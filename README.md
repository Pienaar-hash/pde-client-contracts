# PDE Client Contracts

Published client-facing contracts for systems that integrate with PDE without access to PDE internals.

The first consumer is the Snowfish FSP Portal.

## Directional integration view

```text
CUSTOMER / CHANNEL
        │
        ▼
┌──────────────────────────┐
│ FSP PORTAL               │
│                          │
│ enquiry capture          │
│ enquiry lifecycle        │
│ broker qualification     │
│ immutable NB handoff     │
└────────────┬─────────────┘
             │
             │ PortalNewBusinessCandidate
             │
             │ handoff_id
             │ origin actor
             │ authority-typed declarations
             │ immutable source refs if any
             │ correlation/idempotency key
             ▼
┌────────────────────────────────────┐
│ PDE CANDIDATE / ORIGIN ADMISSION   │
│                                    │
│ idempotent receipt                 │
│ preserve origin                    │
│ allocate case/candidate identity   │
│ validate authority classes         │
│ expose blockers + next owner       │
└──────────────┬─────────────────────┘
               │
               │ only when admission
               │ conditions are satisfied
               ▼
          PDE ACTIVE WORK
               │
               ▼
┌────────────────────────────────────┐
│ PDE SEMANTIC / AUTHORITY KERNEL    │
│                                    │
│ source evidence                    │
│ admitted state + identity          │
│ semantic context/resolution        │
│ transaction authority              │
│ blockers/progression               │
│ consequential capabilities         │
│ decisions + acceptance evidence    │
└──────────────┬─────────────────────┘
               │
               │ client-neutral projection
               ▼
      broker UI / authorised agent

               │
               └──── read-only correlated
                     state/outcome to Portal
```

This diagram is directional. It shows the intended system boundary and ownership flow; it is not a runtime topology or implementation-status map.

## Ownership boundary

```text
                  JOINT CONTRACT
             PortalNewBusinessCandidate
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
       PORTAL / STEFAN          PDE OWNS
       producer envelope        candidate admission
       handoff identity         PDE case identity
       origin provenance        authority validation
       typed declarations       blockers/progression
       genuine source refs      capabilities
       delivery attempts        accepted state
       retries                  reconciliation result
       reconciliation client    downstream authority
       operator feedback
```

The shared contract owns the versioned request/response shapes, correlation identity and compatibility rules. Portal implementation remains on the Portal side of the boundary; PDE admission and insurance authority remain on the PDE side.

## Portal-side New Business tranche

The Portal side can advance as one substantial engineering tranche before PDE receiver work is required:

- produce the candidate deterministically from the immutable New Business handoff;
- preserve `handoff_id`, origin actor/provenance, authority typing and genuine source references where available;
- keep delivery state separate from the immutable handoff;
- build durable outbound/integration records and delivery-attempt history;
- implement retry, restart recovery and correlation/idempotency handling;
- define a configurable outbound adapter boundary for the eventual PDE receiver;
- surface queued, failed, retry and reconciliation states to the Portal operator;
- prove transport, timeout, retry and restart behaviour with a deterministic test receiver; and
- document the Portal-side operating and recovery path.

This is intentionally a cohesive ownership tranche rather than a sequence of micro-issues. The useful review point is when the Portal side is complete enough that further progress genuinely depends on PDE receiver, authentication, response or reconciliation semantics. PDE work can then be implemented against the proven producer boundary rather than anticipated in advance.

## Current contract

[`contracts/fsp-portal/new-business/v0`](contracts/fsp-portal/new-business/v0/README.md)

The repository should remain small: published contracts and the minimum examples/tooling needed to consume them.