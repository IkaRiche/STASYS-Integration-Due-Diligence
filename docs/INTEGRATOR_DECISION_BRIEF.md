# STASYS — Integrator Decision Brief
**Technical discussion package · 24 November 2026**

## The engineering decision

Can a single STASYS system-level configuration **replace or consolidate several resource-intensive onboard computing functions**, while preserving acceptable functional outcomes, independent physical safety authority and retrospective accountability?

The prospective form factor is **one or two modules**. This is a **product target**, not a measured complete-stack implementation.

## The partner's five desired outcomes

1. Civil mission continuity when GNSS or communications are degraded, subject to trustworthy source information and independent failsafe limits.
2. Onboard perception/object continuity with significantly lower full-pipeline computing requirements.
3. Safety regarding obstacles and terrain without overriding existing flight-controller authority.
4. Offline reconstruction of the observation → intent → authorization → action → observed-result chronology, including divergences.
5. Decentralized local cooperative protective function without central leader, host-selected task allocations or a hidden solver.

**System criterion:** reduced *whole-subsystem* mass, electrical power, delay, cost, RAM/Flash and fault exposure when compared to the integrator's existing platform at comparable safety and functional accuracy.

## The computational proposition

```text
O(t+1) = Phi_G(O(t), E(t))
D(t)   = R(O(t+1))
```

This is a **canonical Morphic AI research objective**, not a claimed complete formal specification of every integrated part. Operational structure and acquired causal experience can affect bounded native computation. An external adapter validates observations; it may not secretly preselect the answer. The computation may produce an externally typed proposal, hold or refusal; a separate component retains the physical-action authorization boundary.

**What stays protected:** internal structures, number/composition of computational entities, detailed morphological transformation operators, firmware/source, training/development parameters and protected evidence.

[Read the non-implementation mechanism paper](COMPUTATIONAL_PRINCIPLES.md).

## What is already demonstrable vs what remains a product target

| Evidence source | Current external claim | Full-system ceiling |
|:--|:--|:--|
| DRC physical F411/Matek/H723 benches | Actual UART command-path admission/denial, recovery/reconnect and bounded hardware timings | Not full-system flight safety |
| TMC digital + target-lab results | Qualified bounded mission decisions and selected hardware recomputation | Not an entire GNSS-independent mission |
| Morphic Vision | Synthetic local perception and degradation response | Not live camera software replacement |
| Morphic AI | Scoped causal acquired-state digital behavior | Not general completed autonomy |
| Guardian Veil | Scoped leaderless local causal digital cooperation and effect | Not real deployed multi-vehicle protection |
| StasysOS / separate logs | Scoped deterministic replay and trace integrity work | Not complete real-mission causal forensic reconstruction |

[Detailed evidence matrix](INTEGRATED_EVIDENCE_MATRIX.md) · [public TMC mission](MISSION_CONDUCT_EVIDENCE.md) · [timing](TIMING_EVIDENCE.md).

## What the engineering team can verify without code disclosure

**Proposed review path:** a source-qualified native demonstration under owner control, evaluator-selected permitted challenge cases, independent observation and matched conventional reference, with frozen build and trace provenance. Resource claims are made only on an equivalent **complete** subsystem.

[External data contract](EXTERNAL_INTERFACE_CONTRACT.md) · [Black-box test protocol](BLACKBOX_EVALUATION_PROTOCOL.md) · [Evidence/IP policy](EVIDENCE_ACCESS_AND_IP.md).

## Decision sought

A **technical fit / research-pilot** decision based on one measured safe non-actuating demonstration and a preliminary whole-subsystem baseline. Commercial pricing, platform adaptation, component access and IP licenses belong to a separate agreement.

This briefing does not promise field operation, autonomous target guidance, drone-swarm deployment or airworthiness approval.
