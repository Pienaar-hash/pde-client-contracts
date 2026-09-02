# PDE Client Contracts

This repository publishes the external contracts that client systems can use to integrate with PDE without needing access to PDE internals.

The first consumer is the Snowfish FSP Portal. PDE already has substantial New Business workflow capability; the missing seam is specifically the admission of a Portal-originated New Business candidate into that existing domain.

## FSP Portal → PDE: bird's-eye view

Current position:

- the FSP Portal already owns enquiry capture, enquiry lifecycle, broker qualification and an immutable New Business handoff;
- the v0 producer contract is published here;
- PDE already has source-backed New Business intake, operator capture, issued-policy ingest, comparison, decision, client confirmation and acceptance/baseline flows;
- the Portal-specific PDE candidate/origin-admission receiver, service authentication and external reconciliation contract are still to be connected.

The target system boundary is:

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
             │ v0 producer now → v1 receiving seam later
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

This is the intended **system boundary**, not a claim that PDE's internal packages form a literal serial pipeline.

## Joint contract boundary

For this collaboration, Stefan owns the Portal side of the seam and PDE owns admission and downstream insurance authority.

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
       Portal-side reconcile    downstream authority
       operator transport UI
```

The shared contract owns the versioned request/response shapes, correlation identity and compatibility rules. Neither system may infer the other's authority from transport behaviour.

## Current published contract

The first contract is [`contracts/fsp-portal/new-business/v0`](contracts/fsp-portal/new-business/v0/README.md).

It lets the Portal build its producer, durable delivery/retry state and operator transport loop now. It stops before the still-pending PDE Portal-ingress adapter. When that receiving seam exists, the contract can advance to v1 with the real endpoint, authentication, idempotent reconciliation and PDE candidate response.

## Why this repository exists

The first seam is intentionally small. The value of a separate public repository is that an external client can pin a contract or schema without receiving access to the private PDE implementation. It should stay small: published contracts and the minimum examples/tooling needed to consume them, not a second copy of PDE documentation.
