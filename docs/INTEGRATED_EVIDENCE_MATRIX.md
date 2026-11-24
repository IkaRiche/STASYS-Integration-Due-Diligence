# STASYS — Integrated Evidence Matrix for Technical Evaluation
**External engineering summary · 24 November 2026 · Evidence-backed claims vs product objectives**

> **The buyer is evaluating one system-level capability**, not buying a collection of parts. Results from separate research lines cannot be added together to imply a verified fully integrated product. This matrix is intentionally limited to **observable external behavior** and sanitized custody identifiers. Detailed test vectors, algorithms, firmware and raw private records remain under owner control.

## 1. Buyer outcomes: evidence and qualification ceiling

| Desired integrated result | Closest available evidence | What it supports today | Not yet established |
|:--|:--|:--|:--|
| Mission continuity under missing/degraded GNSS and communications | TMC scoped native and embedded decision traces; one [1,501-record digital session](MISSION_CONDUCT_EVIDENCE.md) | Bounded mission-state continuity and intent/refusal behavior for tested inputs | GPS-independent localization, completed physical route, EW robustness, generic mission success |
| Perception / object continuity with a smaller computing footprint | Morphic Vision local-only **synthetic** perception tests, occlusion and replay interventions | Scoped deterministic response to supplied local observation/degradation primitives | Camera-to-descriptor pipeline, detection/tracking quality on real data, elimination of external vision processors |
| Collision / terrain safety | Independent flight-controller safety authority is explicitly retained; DRC embedded gate separate evidence | Constrained externally authorized outputs and command-path denial in tested channels | End-to-end physical obstacle/terrain detection or avoidance by integrated STASYS |
| Offline reproduction and causal accountability | StasysOS replay/trace tooling; TMC matching run traces; DRC captured real UART events | Scoped software trace reproduction and selected hardware output observation | Whole-flight multimodule reconstruction, completeness of sensor evidence, human-explainable internal causal proof for each result |
| Leaderless cooperative protection | Guardian Veil closed scoped digital causal line, held-out protective effect and tested fault resilience; E006 bounded model fixture | Local functional cooperation without runtime leader election or central task assignment **in the qualified digital models** | General multi-aircraft hardware deployment, real-world protective effectiveness, independent physical swarm replication |
| **Overall hardware consolidation** | DRC small embedded footprints and hardware latency; TMC one scoped hardware timing measurement | Feasibility of some bounded computation on MCU-class hardware | One/two-board integrated package, system-level watts, weight, speed, total bill of materials or reliability advantage |

**Classification:** evidence from digital models, hardware bench and future field integration is kept separate. No system-level flight, operational protection or certified safety claim is made.

## 2. Selected verifiable public statements

### TMC — bounded mission conduct

- **One** continuous digital test session contains **1,501 sequential state records** over a **1,500 s scenario horizon**. It is not 1,501 missions and not evidence of a completed physical 25-minute flight.
- A **separate** STM32H723/Matek bench reported a maximum of **4,997 cycles at 400 MHz = 12.4925 µs** for a specifically scoped recomputation in two cold runs; this excludes the end-to-end sensor/authority/actuator pipeline. The observed traces matched in those runs. No global worst-case execution-time guarantee follows.
- A full-information conventional comparator matched the selected bounded research result. Universal computational or performance superiority is **not established**.

**Public detail:** [mission conduct evidence](MISSION_CONDUCT_EVIDENCE.md) · [timing evidence](TIMING_EVIDENCE.md).

### DRC — physical command-path assurance

The private owning evidence register and associated hardware bench reports record these **distinct, configuration-specific** results:

| Hardware result / scope | Observed result | What must not be inferred |
|:--|:--|:--|
| STM32F411 + real ArduPilot/Matek H7A3-SLIM UART MAVLink v2 | **11/11** test-denied COMMAND_LONG frames were absent from the physically captured output; tested HEARTBEAT warm-path ALLOW **3.55 µs** | A generic certified command gate or flight safety guarantee |
| F411 real FC stream under heartbeat interruption | Recovery-state latch at approximately **3.002 s** in the tested configuration | A verified autonomous safe landing or physical return trajectory |
| STM32H723 UART/MAVLink bench | Local measured **1.345 µs ALLOW** and **2.49 µs DENY** in its specific hardware configuration | Comparable end-to-end timing on a different board |
| Inline fail-passthrough bench with passive NC bypass | At **20 Hz**, one frame lost across the tested abrupt power-loss transition | Guaranteed lossless recovery in all operating conditions |
| STM32 supervised reconnection with real source stream | Output suppression while recovery checks remained pending; permitted forwarding resumed only after tested supervised state | Proof of any integrated multi-component mission continuation |
| Compact security/embedded build | Historically documented approximate **49 KiB Flash** for the stated build configuration | Complete integrated STASYS firmware footprint |

The internal hardware corpus includes original raw UART captures, machine summaries, build identifiers, diagrams and regression evidence. The public matrix records sanitized observations only; the source files are **not mirrored** into this repository. Access to selected original material, if appropriate, requires separate contractual and IP review.

### Morphic Vision — synthetic perception research

- Local-only observation admission, response to occlusion/degradation and deterministic trace differences were tested in a bounded simulated environment.
- The tests were **not** end-to-end real-camera recognition/tracking, physical optical performance or independent proof of external camera-software displacement.

### Morphic AI — causally operative acquired experience

- Scoped digital experiments established that previous lawful interaction can acquire a persistent operative change that causally affects later action under matched current observations.
- The current **Original80 sequential functional 3D A→B→C\*** target, broad generalization and complete product-level autonomous decision capability remain unqualified.

### Guardian Veil — decentralized functional cooperation

- The original digital line is **CLOSED / FROZEN_FUNCTIONALLY_ESTABLISHED** at its scoped level: local protective causal loop, multi-node composition, held-out benefit and resilience in the tested fault family.
- E006 has **PASS** for one bounded locally obtained functional consequence in a physics-only model fixture, with selective causal controls. It does not qualify real sensor hardware or general field performance.
- No central scheduler, chosen leader or hidden host decision is admitted in the accepted local mechanism. This is a **mechanism boundary**, not a blanket performance claim.

## 3. Evidence categories and their owners

| Evidence package | Where a reviewer can start | Source custody |
|:--|:--|:--|
| Public TMC digital session | [Mission conduct report](MISSION_CONDUCT_EVIDENCE.md); [controlled demo](https://tmc.stasysos.eu/lab) (availability not guaranteed) | Original source and extended digital records retained by rights holder |
| Public scoped embedded timing | [Timing report](TIMING_EVIDENCE.md) | Original bench records retained by rights holder |
| DRC physical command-path evidence | This sanitized matrix, plus a **controlled owner-operated live hardware demonstration** | Original F411/Matek UART and H723 logs retained privately; no public source release |
| Morphic Vision synthetic research | This matrix; signed-off sanitized test demonstration to be prepared | Source-owned scientific test and raw evidence retained privately |
| Morphic AI native causal evidence | This matrix; scoped input/outcome comparison to be curated | Source-owned experiments and material-causality evidence retained privately |
| Guardian Veil digital cooperation | This matrix; controlled digital causal playback to be curated | Frozen digital evidence and exact controls retained privately |
| End-to-end buyer baseline | [Black-box evaluation protocol](BLACKBOX_EVALUATION_PROTOCOL.md) | **Not executed** on the partner platform |

## 4. What the buyer can independently inspect

**Now:** open this documentation, evaluate scope, pose black-box challenge inputs, review published numerical limits and specify fair independent baselines.

**Under agreed access:** watch an owner-run native executable or physical bench, choose bounded admissible challenge conditions, collect signed external outputs, challenge selected negative controls, verify hashes and compare with a reference system.

**Not represented as available today:** downloadable production firmware, independent inspection of proprietary internal operators, whole-stack live integration, platform test qualification or certification.

A positive lab test is **not** a claim about an untested integrated platform. Negative scientific evidence is retained in internal custody and remains available for authorized review without being rewritten as positive evidence.

[Computation](COMPUTATIONAL_PRINCIPLES.md) · [External contract](EXTERNAL_INTERFACE_CONTRACT.md) · [Evaluation protocol](BLACKBOX_EVALUATION_PROTOCOL.md) · [Evidence access](EVIDENCE_ACCESS_AND_IP.md).
