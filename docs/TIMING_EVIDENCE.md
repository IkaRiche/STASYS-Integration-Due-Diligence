# Timing: embedded measurement and limits

**Approximately 12.5 µs was the observed maximum for one measured recomputation scope on an STM32H723/Matek bench.** It is not a worst-case execution-time guarantee, a percentile, or the latency of a complete observation-to-outcome loop.

| Item | Observed value |
|:--|:--|
| Board and clock | STM32H723/Matek bench, 400 MHz |
| Public evidence | TRACE_004, two cold runs |
| Measured scope | Scoped mission-decision recomputation only; serial reporting excluded |
| Maximum observed | 4,997 cycles / 400 MHz = 12.4925 µs (approximately 12.5 µs) |
| Decision trace | Two cold runs produced byte-identical decision traces |

Source: [public hardware evidence summary](https://tmc.stasysos.eu/#hardware-evidence). The decision-trace match demonstrates the observed repeatability of that trace in those runs; it does not demonstrate identical timing or characterize the latency distribution.

## What remains unmeasured here

- The public summary does not provide the number of timed observations or a latency distribution. No p50, p95, p99, jitter figure or hardware worst-case bound is claimed.
- Production end-to-end latency is not established. The reported value is not a platform-loop measurement, a scheduling deadline or a throughput rate.
- No guarantee is made for a different target, build, clock, workload or operating conditions.
- The digital session duration and count of state records are not hardware compute measurements.

[Mission conduct evidence](MISSION_CONDUCT_EVIDENCE.md) · [Status & disclosure](STATUS_AND_DISCLOSURE.md)
