# PDE Client Contracts

This repository contains external contracts published by PDE for client systems.

It is not PDE implementation authority. A published contract describes what a client may rely on; it does not prove that a capability is implemented or deployed unless that contract explicitly records an implemented status and an exact PDE implementation boundary.

PDE implementation truth remains in `Pienaar-hash/insurance-policy-engine-mvp`. Client systems must integrate through the versioned contracts published here rather than PDE internals, databases or filesystem state.

Each contract must identify its status, version, publisher, consumer, source PDE boundary and implementation status. Contract-only publications must remain explicit about capabilities that do not yet exist.
