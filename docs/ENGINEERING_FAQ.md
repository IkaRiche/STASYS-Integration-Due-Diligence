# Engineering FAQ — for the existing-platform integration call

**What exactly are we evaluating?** One proprietary **integrated onboard computing capability** intended to consolidate mission continuity, bounded perception/decision functions, independent command assurance and offline forensic replay; a separate leaderless cooperation capability is part of the same system-level evaluation. Demonstrated component evidence exists, but combined product qualification and one/two-board packaging are not yet established.

**Will the flight controller remain authoritative?** Yes: existing physical stabilization, navigation execution and failsafe decisions retain independent authority. The evaluation may test whether other computing responsibilities can be consolidated without reducing actual safety or relying on a hidden external solver.

**Can it run next to our Linux or RTOS application?** Placement is a design question. MCU-native laboratory execution supports feasibility research; no specific board/OS deployment is guaranteed until target measurements and interface tests exist.

**Which protocol do we need?** The team needs to identify its actual data and authority seam. Transport support is not assumed; a versioned adapter must be scoped.

**Can STASYS replace the camera-processing software?** This is a **testable target, not a demonstrated current capability**. Existing Morphic Vision evidence is scoped digital observation/degradation processing, not an independently validated end-to-end sensor ingestion and object-tracking replacement. Whole-system power/compute claims must include any upstream producer still required.

**What happens when GNSS or operator communications fail?** A lost channel does not itself establish whether continuation is possible. The system may be evaluated against the context still valid, but only an independently safe and authorized continuation can proceed. No missing localization information is invented.

**Does the demonstrator establish 25 minutes of completed flight?** No. The existing scenario viewer represents requirements, and the separate laboratory studies have narrower experimental scopes.

**What is the evidence level?** Selected software and embedded components have controlled laboratory research; the partner's entire integration and operational mission are separate qualification subjects.

**Will you disclose internal computational structure, source or firmware?** Not in this public repository. Technical discussion can proceed from interfaces, externally observed behavior and independent acceptance criteria. Any further disclosure is a separate rights-holder decision.

**Can Guardian Veil cooperate without a central leader?** The accepted mechanism is based on native local responses and does not require a runtime master or centralized task allocator. Scoped digital results exist; arbitrary physical swarm protection and platform-level hardware integration are **not established**. A buyer evaluation must specifically exclude host-selected roles and hidden central decisions.

**Can you show that the whole stack is lighter/faster/more reliable?** Not yet as a verified integrated comparison. That requires measurements of both complete stacks under matched function, inputs, safety requirements and environmental conditions; disclosing internal algorithms is not necessary for an external input/output comparison.

## Information requested from integrator

| Engineering topic | Integrator response |
|---|---|
| Platform model and existing civil mission | To be provided |
| Flight/robot controller and firmware revision | To be provided |
| Onboard compute, OS/RTOS and power/resources | To be provided |
| Available non-actuating telemetry and data interfaces | To be provided |
| Valid localization alternatives during degraded GNSS | To be provided |
| Independent completion/outcome feedback | To be provided |
| Controller authority, fail-safe and watchdog requirements | To be provided |
| One decisive bounded shadow-mode evaluation | To be agreed |

Do not post proprietary partner documents, customer mission data or credentials to a public repository.
