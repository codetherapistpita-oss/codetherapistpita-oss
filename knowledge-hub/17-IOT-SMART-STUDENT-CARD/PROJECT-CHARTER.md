# 01 · Project Charter & Research Scope

[← Project home](./README.md) · [Requirements](./REQUIREMENTS-AND-TRACEABILITY.md) · [Implementation plan](./GANTT-CHART.md)

> **Document classification:** Public academic concept documentation · **Status:** Proposed prototype, not an implemented university service · **Revision:** 1.1 · **Updated:** 8 November 2026

## 1.1 Project identification

| Field | Value |
| :--- | :--- |
| Research title | Design and Implementation of an IoT-Based Smart Student Card for Integrated University Services |
| Case study | Kampala International University (KIU) |
| Institution | Kampala International University |
| Academic area | School of Mathematics and Computing · BSc Computer Science |
| Session | Weekend |
| Academic level | Year 3, Semester 2 |
| Proposed supervisor | Eng. Pembe Fahad |
| Proposed deliverable | Centralized four-terminal IoT prototype using a single student card |
| Publication boundary | Public technical synopsis and design artifacts; no institutional production data |

### Research team

| Member | Responsibility |
| :--- | :--- |
| Musinguzi Stanley | Group member — task allocation to be approved |
| Gyagenda Peter Katabalwa | Group member — task allocation to be approved |
| Mwangusha Joseph | Group member — task allocation to be approved |

**Record reconciliation:** The public project uses the later updated topic-submission list. An earlier funding request contains an inconsistent third-member name. The team should resolve that discrepancy before submitting formal signed documents. Registration identifiers and signatures are omitted here.

## 1.2 Problem statement

University services may use separate student identifiers, paper clearances and service-specific verification routines. The study proposes to evaluate whether **one physical NFC-enabled student card** can support consistent identity and service-status checks at selected points while preserving authorization, accountability and resilience.

The extent of these problems at KIU has **not been quantified in this public documentation**; stakeholders and test users would need to validate the baseline during requirements gathering.

## 1.3 Aim

To design and demonstrate a centrally managed, IoT-enabled smart-card prototype that supports **student identification, library eligibility, examination eligibility and simulated finance clearance** at controlled campus-style service terminals.

### Specific research objectives

1. Define the service processes and data required for each terminal.
2. Design an ESP32/PN532 terminal that communicates with a prototype central API.
3. Implement a service-specific authorization decision flow using **synthetic student and card records**.
4. Test rejected, revoked, unknown and offline card scenarios.
5. Evaluate scan-to-decision latency, reliability, response correctness and usability.
6. Document limitations and a conditional path to future integration, subject to KIU authorization.

## 1.4 Scope and boundaries

| In scope for proposed demonstration | Explicitly out of scope |
| :--- | :--- |
| Four service-type terminals | Live KIU finance or examination databases |
| NFC card read and simulated credential mapping | Actual campus-gate access control |
| ESP32 status interface with OLED/LED/buzzer | Real payment transfers or receipts |
| Prototype API, sample database and service rules | Use of production student records without authorization |
| Device authentication and audit-event design | Issuing official KIU cards |
| Functional, negative and offline test plans | Claims of anti-cloning security from UID alone |

### Future enhancement candidates

Attendance, campus gates, general clearance, optional mobile integration, hostel/meal access and hardened offline operation **may be researched later**. They are not part of the four-terminal demonstration acceptance baseline.

## 1.5 Stakeholders and expected artifacts

| Stakeholder | Proposed contribution | Artifact |
| :--- | :--- | :--- |
| Supervisor | Scope and research-method review | Approved project plan |
| Student team | Design, implementation and evaluation | Prototype, source, tests, report |
| Selected service representatives | Validate assumptions where permitted | Use-case feedback |
| Volunteer test participants | Supervised usability feedback | Anonymized observations |
| System administrator role | Demonstrate lifecycle controls | Sample enrollment and revocation records |

## 1.6 Research questions

- Can a single demo credential be resolved consistently across four distinct services?
- Can each terminal receive only the decision it is authorized to request?
- How does the prototype behave when the card is unknown, revoked, or the network is unavailable?
- What latency and reliability are observed under repeated scans?
- What additional cryptographic and governance controls would be needed for real deployment?

## 1.7 Success conditions

A successful academic prototype will show **four observable end-to-end simulated service journeys**, no unauthorized cross-service disclosures in the specified negative tests, traceable audit events, repeatable test data, and a written evaluation of limitations. Results must be recorded after real tests; none are implied here.

---

[Architecture](./ARCHITECTURE.md) · [Service terminals](./SERVICE-TERMINALS.md) · [Security & evaluation](./SECURITY-AND-TESTING.md) · [Project home](./README.md)
