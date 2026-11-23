<p align="center"><img src="assets/stasysos-logo-official.png" alt="STASYSOS — official silver hexagonal circuit emblem and wordmark" width="700"></p>

<p align="center">
  <strong>PROPRIETARY ONBOARD AUTONOMY · ENGINEERING INTEGRATION BRIEF</strong>
</p>

<p align="center">
  <a href="README_RU.md">Русская версия</a> ·
  <a href="docs/CIVIL_K01_PRE_READ.md">Civil K-01</a> ·
  <a href="docs/INTEGRATION_INTERFACE.md">Interface</a> ·
  <a href="docs/ENGINEERING_FAQ.md">Engineering FAQ</a> ·
  <a href="docs/STATUS_AND_DISCLOSURE.md">Qualification</a>
</p>

<p align="center">
  <a href="https://github.com/IkaRiche/STASYS-Integration-Due-Diligence/actions/workflows/validate.yml"><img src="https://github.com/IkaRiche/STASYS-Integration-Due-Diligence/actions/workflows/validate.yml/badge.svg" alt="Documentation integrity workflow"></a>
</p>

## Mission continuity, designed for integration

**A separate onboard mission-conduct capability for an existing autonomy platform.**

STASYS develops proprietary deterministic computing technology for resource-constrained autonomous systems. The proposed integration allows a mission core to receive admitted operational context, retain an assigned objective and form bounded mission-intent proposals, while the platform's own controller remains responsible for motion, authorization and safety.

This is a **technical pre-read for system integrators**, not an offer of source code or a claim of a certified, flight-ready product. External interfaces and observable acceptance criteria are available for discussion; the internal computation remains proprietary.

<table>
<tr>
<td width="33%" valign="top">
<strong>01 · Mission continuity</strong><p>Retain the assigned objective and evaluate permissible continuation when conditions change.</p>
</td>
<td width="33%" valign="top">
<strong>02 · Existing platform preserved</strong><p>Keep sensing, navigation, stabilization, execution and independent safety authority in the incumbent stack.</p>
</td>
<td width="33%" valign="top">
<strong>03 · Verifiable evaluation</strong><p>Start with a non-actuating, bounded test using real interface assumptions and independent outcome feedback.</p>
</td>
</tr>
</table>

## A defined engineering case — Civil K-01

**The evaluation scenario already exists.** Civil K-01 describes a 25-minute civilian mission with six phases and five timed evaluation windows, supported by a requirements visualization and separate controlled laboratory research.

<img src="assets/civil-k01-timeline.svg" width="100%" alt="Civil K-01: preparation, departure, degradation, obstacle event, service window and return or closure — six schematic phases"/>

The viewer communicates *the intended operating sequence*. The separate laboratory work examines bounded computational behavior. Neither alone establishes an end-to-end completed physical flight.

**[Explore the Civil K-01 engineering case →](docs/CIVIL_K01_PRE_READ.md)**

## Architecture at the integration boundary

<img src="assets/integration-boundary.svg" width="100%" alt="Existing observations feed a STASYS mission-conduct core, which proposes non-actuating intents through the platform's independent safety authority and controller; verified outcomes return as feedback"/>

The diagram is a **candidate responsibility model**, not an implemented data protocol. The interface is intended to preserve these distinctions:

| System responsibility | Integration position |
|:--|:--|
| Observations, localization and data validation | Existing platform |
| Mission objective and bounded continuation proposals | **STASYS TMC** — proprietary mission-conduct component |
| Execution permission and failsafe decisions | Existing independent authority |
| Flight / robot motion | Existing controller and executor |
| Evidence of action outcome | Independently verified platform feedback |
| Optional command-path assurance | Separate **DRC/SRC** assessment where required |

**TMC is not an autopilot.** Its output is a proposal rather than authority to actuate. A partner's existing safety boundary and control logic are not bypassed.

**[Read the proposed interface contract →](docs/INTEGRATION_INTERFACE.md)**

## Technical review — four documents

<table>
<tr>
<td width="50%" valign="top">
<strong>01 / Evaluation scenario</strong>
<p>Define the known civil mission, relevant operating interruptions and what the visual laboratory does and does not demonstrate.</p>
<a href="docs/CIVIL_K01_PRE_READ.md">Civil K-01 briefing →</a>
</td>
<td width="50%" valign="top">
<strong>02 / Integration architecture</strong>
<p>Candidate inputs and outputs, authority boundary, feedback responsibilities and non-actuating evaluation gates.</p>
<a href="docs/INTEGRATION_INTERFACE.md">Integration interface →</a>
</td>
</tr>
<tr>
<td valign="top">
<strong>03 / Engineering answers</strong>
<p>Processor placement, protocol assumptions, localization degradation, perception and the information needed from the platform team.</p>
<a href="docs/ENGINEERING_FAQ.md">Engineering FAQ →</a>
</td>
<td valign="top">
<strong>04 / Qualification and rights</strong>
<p>Readiness scope, independent testing, restricted disclosures and the boundary between evaluation and licensing.</p>
<a href="docs/STATUS_AND_DISCLOSURE.md">Status &amp; disclosure →</a>
</td>
</tr>
</table>

## The next technical decision

For the existing Civil K-01 scenario, the practical objective is to agree on **one authentic observation-to-intent-to-feedback seam** in the partner's present platform. An initial shadow-mode comparison can then measure a STASYS candidate against an equal-information existing mission executive without transferring execution authority.

Selected software and embedded-control mechanisms have controlled laboratory evidence. **Platform-specific compatibility and complete mission-level field qualification remain separate acceptance requirements.** This public package provides no proprietary implementation, unrestricted test image, patent license or commercial terms.

<p align="center"><strong>STASYS · EXTERNAL INTERFACES, CONTROLLED EVIDENCE, PROPRIETARY COMPUTATION</strong></p>

<sub>Public technical pre-read · 23 November 2026 · <a href="LEGAL.md">Rights and restrictions</a></sub>
