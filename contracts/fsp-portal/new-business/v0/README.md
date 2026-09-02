# FSP Portal → PDE New Business Candidate v0

**Portal producer contract:** published  
**PDE Portal-specific ingress:** pending  
**PDE downstream New Business workflow:** existing

This v0 contract lets the Snowfish FSP Portal build its side of the New Business integration now, without needing access to PDE internals and without waiting for the Portal-specific PDE receiver.

The important distinction is narrow: **PDE New Business is not a ghost.** PDE already has source-backed New Business intake, operator shell/capture, instruction persistence, issued-policy ingest, comparison, decision, client confirmation and acceptance/baseline flows. What does not yet exist is the adapter that receives this Portal-originated candidate before policy identity and active-work admission.

The downstream PDE capability was rechecked at `4b3cd6facecf83152d17ee6234516737d937ea9b`. The original v0 contract was derived from PDE main `dfe95e7294b0ea804fcee9a384dbd6680b06946b`, internal contract-source `c436ae5b0454c5e10ec6d508f309407423301bc3`, and Portal producer boundary `e0769ccf6fcb2cc82b6702560e55860d2053d239`.

## Where v0 fits

```text
FSP Portal
  enquiry + qualification
          │
          │ immutable handoff
          ▼
PortalNewBusinessCandidate v0
          │
          │ producer/delivery seam Stefan can build now
          ▼
[ Portal-specific PDE candidate/origin admission — pending ]
          │
          ▼
existing PDE New Business domain
  capture → issued-policy ingest → compare → decide → confirm → accept
```

The target v1 receiving seam is shown in the repository-level [bird's-eye view](../../../../README.md).

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

The declaration snapshot is explicitly typed as:

`portal_captured_declaration`

That means the Portal captured and preserved the declaration. It does not promote the declaration into insurer-issued evidence or admitted policy state.

## What Stefan can build now

Against v0, the Portal can independently implement:

- deterministic candidate construction from the immutable handoff;
- origin actor/provenance preservation;
- a separate durable outbound/integration record;
- delivery-attempt history;
- retry and restart-safe persistence;
- operator-visible queued/failed transport state;
- Portal-side correlation by `handoff_id`; and
- a local HTTP test receiver for transport and recovery proof.

The local receiver is only a transport test double. The Portal does not need to wait for a real PDE endpoint to prove its own producer, persistence, retry and operator loop.

## Current stop line

Until PDE publishes the receiving contract, the Portal should not invent:

- a `policy_ref` merely to satisfy an existing PDE operator shell;
- a PDE candidate/case ID;
- PDE endpoint or authentication details;
- PDE blocker, progression or capability vocabulary; or
- a claim that successful transport means PDE admission or active work.

`handoff_id` is the cross-system correlation identity, not an insurer policy identity. Genuine source references may be carried when they really exist; Portal-captured declarations remain declarations.

## Target v1 seam

v1 should connect the producer to a real PDE candidate/origin-admission boundary with:

- service authentication;
- idempotent receipt keyed by the external correlation identity;
- a stable PDE candidate/case identity;
- authority validation;
- a bounded admission/blocker/next-owner response;
- deterministic reconciliation after timeout or retry; and
- a read-only correlated PDE state/outcome that the Portal can render without recomputing PDE authority.

The Portal owns its producer, handoff, delivery attempts, retries and operator transport feedback. PDE owns candidate admission, PDE identity, authority validation, blockers/progression, capabilities and accepted insurance state. Reconciliation is a joint protocol: the Portal initiates and records it; PDE owns the authoritative result.
