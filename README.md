# STASYS — Technical Integration Pre-Read

**Independent onboard mission continuity and execution assurance**  
**Public engineering overview · 23 November 2026**

STASYS develops proprietary deterministic computing components for resource-constrained autonomous systems. This pre-read is intended for engineering teams evaluating an **existing** drone, robotic or industrial autonomy platform. It describes external responsibilities and an evaluation path, not internal algorithms, module internals or implementation source.

## The already-defined evaluation: Civil K-01

The discussion concerns an existing, bounded **25-minute civilian mission scenario**, rather than selecting an unspecified use case. Its requirements visualization and separate laboratory research provide a concrete starting point for platform mapping. The visualization is a requirements aid and does not constitute a completed field mission.

**[Read Civil K-01](docs/CIVIL_K01_PRE_READ.md)** · **[Proposed integration boundary](docs/INTEGRATION_INTERFACE.md)** · **[Engineering Q&A](docs/ENGINEERING_FAQ.md)** · **[Evidence and access](docs/STATUS_AND_DISCLOSURE.md)** · **[Russian overview](README_RU.md)**

## Integration concept

```text
Existing sensors / localization / mission information
                    |
          Validated, typed context
                    |
             [ STASYS TMC ]
         Proprietary mission core
                    |
           Bounded mission intent
                    |
     Existing authorization / safety
                    |
       Existing controller / executor
                    |
       Verified outcome and feedback
                    +----> validated context
```

**STASYS TMC** is the candidate mission-conduct component. It is intended to retain a previously authorized mission objective, evaluate a changing operational context and propose admissible continuations. It **does not directly control actuators**, replace the vehicle's flight-control stabilization or bypass incumbent safety interlocks.

**DRC/SRC**, a separate STASYS technology direction, can be considered where independent command assurance and recovery are required. Its integration is **not a prerequisite** for a read-only TMC fit study. The partner's existing authorization chain can remain in place.

## What the integration team can assess now

| Topic | What is provided in this public overview |
|---|---|
| Functional placement | Separation of onboard mission intent from physical vehicle control |
| Input expectations | Required data categories, freshness, provenance and source quality |
| Output expectations | Bounded intent, hold/refusal and feedback correlation |
| Existing system preservation | Controller, navigation and safety functions remain with the platform |
| Verification | Reproducible laboratory evaluation and a proposed partner-specific shadow-mode test |
| Commercial/IP boundary | Proprietary black-box evaluation; no source or implementation rights granted |

**Current qualification:** selected deterministic mission and embedded-control mechanisms have laboratory evidence; platform-specific compatibility and mission-level field qualification require separate acceptance tests. This repository is not a declaration of a certified, flight-ready integration.

## Recommended reading order

1. [Civil K-01 scenario and lab distinction](docs/CIVIL_K01_PRE_READ.md)
2. [Integration boundary and proposed information contract](docs/INTEGRATION_INTERFACE.md)
3. [Engineering FAQ and platform information needed](docs/ENGINEERING_FAQ.md)
4. [Evidence, qualification and disclosure boundary](docs/STATUS_AND_DISCLOSURE.md)

**Contact and access:** evaluations and technical demonstrations are subject to the rights holder's separate approval. This repository conveys no software, patent or technology license. [Rights](LEGAL.md).
