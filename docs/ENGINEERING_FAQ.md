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

## Direct answers to the computational engineering questions

**What mathematics runs inside?** The LMA research objective describes lawful native state evolution with a bounded observable readout: `O(t+1)=Phi_G(O(t),E(t)); D(t)=R(O(t+1))`. This explains the computational principle, not the protected algebraic operators or a published common binary runtime. [Mechanism paper](COMPUTATIONAL_PRINCIPLES.md).

**Is this ML, an LLM or a deterministic scripted controller?** The bounded native mechanism described here is not a generative next-token model. Causally acquired operative structure affects behavior in scoped tests. A conventional implementation can emulate a finite behavior; no universal superiority claim is made. [Mathematics and comparisons](COMPUTATIONAL_PRINCIPLES.md).

**Precisely what do you need as input?** Authorized mission and constraints, typed provenance-bearing observations, resource/capability availability and separately verified action outcomes. Validity, freshness, time base, sensor reference frame and authority must be fixed with the partner. This is a **candidate external semantic contract, not the released live API**. [Input table](EXTERNAL_INTERFACE_CONTRACT.md).

**What comes out?** Bounded non-actuating mission intent, hold/refusal, and function-specific status or command-gate disposition where that separate capability is qualified. The flight controller and independent safety authority retain physical execution ownership. [Output table](EXTERNAL_INTERFACE_CONTRACT.md).

**What happens inside?** External admission → proprietary law-constrained native computation → observable typed expression → independent authority → externally verified consequence. No implementation composition, internal quantities or operator definitions are disclosed. [External responsibility model](COMPUTATIONAL_PRINCIPLES.md).

**Can we verify it without the source code?** The owner can demonstrate a **qualified existing native capability** with fixed build provenance, independent external observation, allowed reviewer-chosen variations and appropriate controls. A self-service complete-stack lab is **proposed, not delivered**. [Evaluation protocol](BLACKBOX_EVALUATION_PROTOCOL.md).

**Can we replay the entire flight and know why every decision happened?** Not yet as a qualified integrated system. Scoped deterministic logs and replay exist; a complete causal explanation requires sufficient admitted input and external outcome records, not just matching hash values. [Evidence matrix](INTEGRATED_EVIDENCE_MATRIX.md).

**What proves the complete system is lighter, cheaper, faster and more reliable?** No existing isolated test proves that. We need a matched **whole-subsystem** baseline including sensor preprocessing, supporting compute, actual power and measured functional accuracy. [Comparison protocol](BLACKBOX_EVALUATION_PROTOCOL.md).

**Where are source-level proof objects?** Preserved in controlled owner custody. This public package provides an evidence index and verification scope. A separately authorized independent audit may be negotiated; no executable access is granted here. [Access policy](EVIDENCE_ACCESS_AND_IP.md).

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
