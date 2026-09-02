#!/usr/bin/env python3

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_ROOT = ROOT / "contracts" / "fsp-portal" / "new-business" / "v0"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    metadata = load_json(CONTRACT_ROOT / "contract.json")

    required_metadata = {
        "contract_id",
        "version",
        "status",
        "implementation_status",
        "publisher",
        "consumer",
        "pde_main_boundary_sha",
        "internal_contract_source_sha",
        "portal_boundary_sha",
        "schema",
        "valid_examples",
        "invalid_examples",
    }
    missing = sorted(required_metadata - metadata.keys())
    if missing:
        raise SystemExit(f"contract metadata missing keys: {', '.join(missing)}")

    if metadata["status"] != "contract_only":
        raise SystemExit("v0 status must remain contract_only")
    if metadata["implementation_status"] != "not_implemented":
        raise SystemExit("v0 implementation_status must remain not_implemented")

    schema = load_json(CONTRACT_ROOT / metadata["schema"])
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    for relative_path in metadata["valid_examples"]:
        example = load_json(CONTRACT_ROOT / relative_path)
        errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))
        if errors:
            joined = "; ".join(error.message for error in errors)
            raise SystemExit(f"valid example failed {relative_path}: {joined}")

    for relative_path in metadata["invalid_examples"]:
        example = load_json(CONTRACT_ROOT / relative_path)
        errors = list(validator.iter_errors(example))
        if not errors:
            raise SystemExit(f"invalid example unexpectedly passed: {relative_path}")

    invalid_authority = load_json(CONTRACT_ROOT / "examples" / "candidate.invalid-authority.json")
    authority_errors = [
        error
        for error in validator.iter_errors(invalid_authority)
        if list(error.path) == ["declarations", "authority_kind"]
    ]
    if not authority_errors:
        raise SystemExit("invalid authority example did not fail on declarations.authority_kind")

    print("contract validation passed")


if __name__ == "__main__":
    main()
