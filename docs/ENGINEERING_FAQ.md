# Engineering FAQ — for the existing-platform integration call

**What exactly would we integrate?** Initially a separately evaluated proprietary onboard **mission-conduct component**, not an entire replacement flight stack.

**Will our autopilot, navigation and safety logic remain intact?** Yes. The proposal is non-actuating and must pass the incumbent execution authority. Any inline command gate is a separate assessment.

**Can it run next to our Linux or RTOS application?** Placement is a design question. MCU-native laboratory execution supports feasibility research; no specific board/OS deployment is guaranteed until target measurements and interface tests exist.

**Which protocol do we need?** The team needs to identify its actual data and authority seam. Transport support is not assumed; a versioned adapter must be scoped.

**Is raw camera video necessary?** Not to evaluate the mission-conduct responsibility. A qualified upstream producer may supply typed observation data with provenance and quality.

**What happens when GNSS or operator communications fail?** A lost channel does not itself establish whether continuation is possible. The system may be evaluated against the context still valid, but only an independently safe and authorized continuation can proceed. No missing localization information is invented.

**Does the demonstrator establish 25 minutes of completed flight?** No. The existing scenario viewer represents requirements, and the separate laboratory studies have narrower experimental scopes.

**What is the evidence level?** Selected software and embedded components have controlled laboratory research; the partner's entire integration and operational mission are separate qualification subjects.

**Will you disclose internal computational structure, source or firmware?** Not in this public repository. Technical discussion can proceed from interfaces, externally observed behavior and independent acceptance criteria. Any further disclosure is a separate rights-holder decision.

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
