# FSP Portal → PDE New Business Candidate Contract v0

**Status:** `contract_only`

**PDE main boundary inspected:** `dfe95e7294b0ea804fcee9a384dbd6680b06946b`

**Internal PDE contract-source boundary:** `c436ae5b0454c5e10ec6d508f309407423301bc3`

**Portal producer boundary inspected:** `e0769ccf6fcb2cc82b6702560e55860d2053d239`

This package publishes the narrow contract that the Snowfish FSP Portal may build against while PDE New Business candidate admission is not yet implemented.

It is deliberately a **v0 producer boundary**, not a claim that PDE currently exposes a receiver. PDE implementation remains authoritative in `insurance-policy-engine-mvp`. The existence of this schema or example does not establish a deployed endpoint, service authentication, PDE candidate identity, admission state, blocker state, `/work` visibility or accepted policy authority.

## Purpose

The contract allows the Portal to prepare a truthful outbound candidate and its own delivery/retry/operator loop without importing PDE code or inventing PDE semantics.

The v0 envelope is derived only from the Portal's existing durable New Business handoff. It preserves the Portal handoff identity and captured enquiry provenance while making the authority class explicit.

## Candidate contract

Schema:

`fsp-portal-new-business-candidate-v0.schema.json`

Valid example:

`examples/candidate.valid.json`

All values under `declarations` carry one v0 authority classification:

`portal_captured_declaration`

That classification means only that the Portal durably captured the declaration and preserved it in the New Business handoff. It does **not** mean the value is insurer-issued evidence, admitted policy state, broker advice, a client election recognised by PDE, or a verified canonical fact.

## Hard negative guarantees

```text
Portal handoff != PDE policy
Portal handoff != PDE candidate admission
transport success != domain admission
handoff_id != policy_ref
portal-captured declaration != insurer/source-document evidence
candidate creation != /work visibility
candidate creation != baseline
candidate creation != comparison
candidate creation != accepted policy state
```

The schema intentionally contains no `policy_ref`, PDE case/candidate ID, comparison ID, blocker state, capability state or acceptance state.

## What the Portal may implement against v0

The Portal may independently implement:

- deterministic construction of the v0 candidate from an immutable handoff;
- an append-only outbound/integration record separate from the handoff itself;
- queued/not-attempted and transport-attempt state;
- retry bookkeeping and attempt history;
- restart-safe persistence;
- operator-visible transport failure state;
- reconciliation by its own `handoff_id` once a real PDE reconciliation contract exists; and
- a deterministic local HTTP test receiver for **transport proof only**.

A local test receiver must not be described as PDE and must not return invented PDE admission, blocker, policy or `/work` semantics.

The original Portal handoff remains immutable. Delivery state must be a separate record/projection.

## Deliberately unresolved until v1

v0 does **not** specify:

- a PDE URL or route;
- service-to-service authentication;
- a PDE candidate/case identity;
- HTTP success/admission status semantics;
- PDE idempotency implementation;
- PDE rejection reason codes;
- blocker or progression vocabulary;
- reconciliation response shape;
- active-work admission rules;
- policy identity creation;
- downstream CommunicationPlan, quote, comparison, decision or baseline behaviour; or
- a PDE → Portal authoritative outcome projection.

Those items require a real PDE receiving implementation and proof. They must not be guessed by the Portal.

## v1 graduation rule

This contract may graduate to v1 only when PDE has a merged receiving implementation that proves, at an exact PDE commit boundary:

1. authenticated receipt of this candidate family;
2. idempotency on an explicit external correlation contract;
3. deterministic reconciliation after lost/ambiguous responses;
4. preservation of Portal declaration authority without promotion to insurer evidence;
5. negative proof that receipt alone creates no policy authority, baseline, comparison or active `/work` state; and
6. an operator-visible disposition for every non-terminal received candidate.

At v1, the package must name the exact implementing PDE commit and the implemented request/response/authentication/reconciliation contracts.

## Ownership

- FSP Portal owns construction of the producer envelope, its immutable handoff, outbound delivery attempts and Portal operator visibility.
- PDE owns receiving/admission semantics, PDE identities, blockers/progression, consequential capabilities and admitted insurance state.
- Neither side may infer the other's authority from transport behaviour.
