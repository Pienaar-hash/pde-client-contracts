# FSP Portal → PDE New Business Candidate v0

This contract defines the producer envelope that the Snowfish FSP Portal can build from its existing immutable New Business handoff.

It fixes the Portal-side shape and correlation identity without prescribing the PDE receiver.

## Candidate envelope

Schema:

`fsp-portal-new-business-candidate-v0.schema.json`

Synthetic example:

`examples/candidate.valid.json`

The candidate preserves:

- the immutable Portal `handoff_id`;
- source enquiry and requirement identities;
- the handoff creation time; and
- the captured declaration snapshot.

The declaration snapshot is typed as:

`portal_captured_declaration`

That classification preserves the authority of the captured value as a Portal declaration. Genuine source references may be carried when they actually exist.

`handoff_id` is the cross-system correlation identity. It is not an insurer policy identity.

## Portal-side work

The Portal may build the complete producer and delivery side around this v0 envelope, including durable outbound state, attempt history, retries, restart recovery, operator feedback, correlation and a configurable adapter boundary.

The repository-level [directional integration view](../../../../README.md) shows where that work is intended to lead and the ownership split across the seam.

A deterministic local receiver may be used to prove Portal transport and recovery behaviour.

## PDE-dependent boundary

The following are left to the receiving contract because they belong to the PDE side of the seam:

- PDE endpoint and service authentication;
- PDE candidate/case identity;
- admission response and blocker/progression vocabulary;
- authoritative reconciliation response;
- active-work admission; and
- correlated downstream state/outcome projection.

The Portal should not invent those semantics to complete its producer-side tranche.

## Next contract step

When the Portal tranche reaches this boundary, the receiving contract can add the PDE endpoint, authentication, idempotent receipt/reconciliation and candidate response required for live integration.