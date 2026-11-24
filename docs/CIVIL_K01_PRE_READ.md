# Civil K-01 — Predefined civilian mission integration case

**Purpose:** map an already-specified 25-minute civil autonomy scenario onto the integrator's actual platform and independently verify one feasible mission-continuity function.

## Requirement outline

The existing scenario uses a **1,500-second time horizon**, six phases and five timed evaluation windows. The windows are review points, **not evidence of completed charging or contact cycles**.

| Scenario phase | What the platform integration must account for |
|---|---|
| Preparation | Vehicle and controller readiness, validated mission assignment and sensor status |
| Departure | Incumbent controller takes off and carries out authorized movement |
| Degraded observations or communications | Preserve objective, distinguish missing data from invalid action, respect existing failsafe |
| Obstacle-related event | Consume trustworthy locally produced sensing, not fabricated coordinates or obstacle solutions |
| Service infrastructure encounter | Distinguish a proposed visit, physical interaction and independently observed successful outcome |
| Return / closure | Independent confirmation of terminal outcome, or explicit bounded refusal when evidence is insufficient |

## Existing work, correctly described

- A **requirements visualization** presents the civil scenario and source-defined time windows.
- **Separate bounded laboratory studies** have exercised deterministic onboard intent and external enforcement semantics under controlled input and feedback conditions.
- The full, closed-loop, platform-specific 25-minute physical mission has **not** been qualified by the visualization or those individual laboratory studies.

Available demonstrations may be shown by the rights holder in a controlled review. A display timeline, test trace or generated intent must never be represented as independent proof of a real-world completed mission.

## Concrete technical fit questions

1. Which controller, firmware and onboard interfaces are available for mirrored observations and non-actuating integration?
2. What navigation and observation-quality evidence remains valid during communications or GNSS degradation?
3. Which independently observed execution outcomes can be returned to the mission core?
4. Who authorizes or blocks execution, and what existing safety conditions must be preserved?
5. Which **one** civilian interval can first be compared against an equal-information conventional mission executive in shadow mode?

**Goal of the meeting:** an interface fit/no-fit decision and the next authorized bench acceptance criterion, not general product discovery or an implied field-deployment commitment.

[Interface](INTEGRATION_INTERFACE.md) · [Engineering FAQ](ENGINEERING_FAQ.md) · [Mission conduct evidence](MISSION_CONDUCT_EVIDENCE.md) · [Timing evidence](TIMING_EVIDENCE.md)
