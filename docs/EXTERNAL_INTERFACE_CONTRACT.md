# STASYS — External Interface Contract (Candidate)
**Typed boundary for technical due diligence · v0.1 · PROPOSED, not a released wire protocol**

This document answers **"What data does STASYS need, what does it produce, and who is responsible for the actual outcome?"** It specifies a *candidate semantic envelope* for an integrated system-level evaluation. It is **not** an existing binary ABI, Rust struct, published MAVLink dialect, delivered driver, or evidence that every function below is implemented in one runtime.

## 1. External responsibility model

```text
Platform sources -> source-specific validators -> admitted factual context
                                                      |
                                                      v
                                         [PROPRIETARY STASYS]
                                                      |
                                                      v
                                       bounded non-actuating result
                                                      |
                                                      v
                                    independent authority / flight controller
                                                      |
                                                      v
                                     independently measured result
                                                      |
                                                      +--> factual feedback
```

An adapter may validate, timestamp, normalize and reject *facts*. It may **not** precompute a mission decision and attribute that answer to the proprietary computation. It must not quietly supply privileged world truth or undisclosed task solutions.

## 2. Proposed input categories

| Input category | Essential semantic fields (examples, not a wire schema) | Contract condition |
|:--|:--|:--|
| **Mission assignment** | `mission_id`, permitted goal type, completion criterion, valid time interval | Must originate from an authorized source; objective is not inferred from arbitrary text |
| **Permitted operating envelope** | Allowed capability categories, resource limits, applicable restrictions | Separate from deciding which action is useful |
| **Platform observation** | Observation kind, source identity, measurement timestamp, frame/units when relevant, validity/uncertainty | Stale, contradictory, unavailable and untrusted values are distinguished |
| **Perception descriptor** | Source type, bounded local observation descriptor, timestamp, validity, continuity/degradation indicator | May be produced by an external sensor/primitive processor; raw camera-to-descriptor autonomy is *not currently qualified* |
| **Platform health** | Power/resource status, compute health, availability flags, validity/freshness | Actual source data, not a simulator-supplied success flag |
| **Execution feedback** | `intent_id` correlation, authorization outcome, performed/not performed, independently observed consequence and evidence source | "Proposed" never means "executed"; "executed" never automatically means "goal achieved" |
| **Local cooperation observation** | Locally admitted environmental change / admissible bounded expression from another participant | No centralized leader, global solution or externally assigned winning responder is assumed |

Data types can be binary and compact; human-readable names above are for review only. Transport, serialization, maximum sizes, rates, time base, reference frames, ownership of sensor preprocessing and invalid-data semantics must be fixed with the integrator before ABI publication.

## 3. Proposed output categories

| Output | Meaning | Who owns the next step |
|:--|:--|:--|
| `MISSION_INTENT` | Bounded proposed continuation within assigned goal and admitted context | Separate platform authorization |
| `HOLD` | Do not propose additional action until required information or permission is available | Existing controller and operator policy |
| `REFUSAL` | No admissible continuation under current conditions | Platform safety authority decides safe handling |
| `PERCEPTION_STATUS` | Bounded local observation/degradation descriptor (only if qualified) | Consumer must validate suitability |
| `ASSURANCE_DISPOSITION` | Command-path allow/deny/drop/recovery state (within a DRC-tested boundary) | Only the specific integrated gate owns its actual channel |
| `REPLAY_RECORD` | Provenance, sequencing and externally observable decision/outcome evidence | Audit tool, not the mission solver |

These are **categories of outputs across the proposed integrated capability**, not necessarily fields simultaneously emitted by one current executable.

## 4. Minimal externally observable record (illustrative)

```text
record_version       "review-0.1"          // presentation label only
session_id           opaque session handle
sequence             monotone review index
time                 timestamp + time-base identifier
source               provenance of measured/admitted input
input_validity       valid | degraded | stale | unavailable | rejected
disposition          intent | hold | refusal | assurance outcome
correlation          external intent/result handle where applicable
external_effect      not_observed | partial | verified | failed
build_commitment     owner-held build identifier / digest
integrity            externally verifiable record-chain digest (proposed)
```

This is an **auditable evidence-envelope proposal**, not a normative live message definition. It must not be mistaken for internal state, Morphic Memory or a certified post-flight recorder.

## 5. Uncertainty, timing and fault rules

- Missing observation is not permission to invent a coordinate, object identity or successful action.
- A sensor datum without known validity, age or source cannot silently become authoritative.
- A continuing mission objective does not confer execution authority on the computing core.
- The meaning of "completion" must be checked against an independent outcome.
- Resource, power and latency limits must be measured on the **actual target and full pipeline**, not inferred from a single isolated function.
- A replay hash detects some differences; it does **not alone explain the internal cause** of every response or prove recorded input completeness.

## 6. Questions needed for an implementation-specific contract

**Platform:** controller, compute board, OS/RTOS, memory/power budget, independent safety authority.  
**Observation:** available factual sources, update rates, timestamping, units/frames, uncertainty and invalid-data policies.  
**Interface:** candidate transport (not assumed supported), maximal payload/rate, buffer ownership, loss/restart protocol.  
**Evaluation:** one permitted non-actuating civil test, independent ground truth, comparator and success criterion.  
**Audit:** evidence retention period, offline reconstruction need, key protection and reviewer access controls.

## 7. Existing evidence vs proposed integration

Specific native mission-conduct experiments and command-gate hardware tests exist. Full-stack multi-function live integration, real-sensor perception replacement, GNSS-free end-to-end navigation and deployed cross-module flight forensic reconstruction remain **distinct qualification targets**.

[Mathematical principles](COMPUTATIONAL_PRINCIPLES.md) · [Evidence](INTEGRATED_EVIDENCE_MATRIX.md) · [Black-box assessment](BLACKBOX_EVALUATION_PROTOCOL.md).
