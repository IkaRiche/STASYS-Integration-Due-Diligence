# Proposed integration boundary — proprietary black-box component

This is a functional **contract proposal**, not a published ABI, driver, message schema or production integration specification.

```text
Existing information producer -> admitted typed context -> [STASYS TMC]
                                         [STASYS TMC] -> mission-intent proposal
Proposal -> platform authorization and safety -> existing controller / executor
Existing measured outcome -> validated feedback -> [STASYS TMC]
```

## Inputs to be mapped

| Category | What an integration adapter must preserve |
|---|---|
| Mission assignment | Externally authorized goal, constraints and completion criterion |
| Observations | Data type, source, freshness, validity/uncertainty and relevant reference frame |
| Platform capabilities | Currently available action classes, health and resource limits |
| Safety constraints | Existing controller restrictions and authority boundaries |
| Execution feedback | Independent result/correlation, including failure and partial outcome |

An adapter translates facts, not decisions. It must not silently choose the next mission continuation and label the result as STASYS computation.

## Outputs to be evaluated

**Bounded mission intent**, **hold/refusal** and **traceable disposition**. These are non-actuating proposals. Execution requires explicit independent permission from the incumbent controller/authority. A transport-specific implementation must be assessed with the partner; no automatic support is asserted for any version of MAVLink, ROS 2, PX4, ArduPilot, CAN, UART or proprietary protocols.

## Qualification gates

1. **Interface fit:** verify input and output owners, data availability, freshness and failure behavior.
2. **Shadow mode:** observe decisions without physical actuation. Run an equal-information incumbent baseline.
3. **Negative and replay tests:** stale, contradictory and absent observations, rejected proposals and partial outcomes.
4. **Resource measurements:** target- and build-specific flash/RAM, CPU/latency, boot/recovery and power behavior.
5. **Separate platform acceptance:** only an independently authorized later test may claim real outcome or field suitability.

The candidate mission core does not create missing localization, defeat a platform failsafe, or confer physical authority. Existing system safety cases and relevant legal requirements remain binding.
