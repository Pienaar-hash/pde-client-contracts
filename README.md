# PDE Client Contracts

Published client-facing contracts for systems that integrate with PDE without access to PDE internals.

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

Direction only; not runtime topology.

## Ownership boundary

```text
                  JOINT CONTRACT
             PortalNewBusinessCandidate
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
          PORTAL OWNS            PDE OWNS
          producer envelope      candidate admission
          handoff identity       PDE case identity
          origin provenance      authority validation
          typed declarations     blockers/progression
          genuine source refs    capabilities
          delivery attempts      accepted state
          retries                reconciliation result
          reconciliation client  downstream authority
          operator feedback
```

The shared contract owns the versioned request/response shapes, correlation identity and compatibility rules.

## Current contract

[`contracts/fsp-portal/new-business/v0`](contracts/fsp-portal/new-business/v0/README.md)
