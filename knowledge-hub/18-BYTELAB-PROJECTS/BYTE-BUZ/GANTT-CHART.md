# 06 · Proposed Byte Buz Development Roadmap & Gantt

[← Project home](./README.md) · [Architecture](./SYSTEM-ARCHITECTURE.md) · [Feature map](./FEATURES-AND-SCREENS.md)

> [!IMPORTANT]
> **Planning illustration, not an agreed delivery contract.** The earlier Byte Buz Master Prompt v1.0 defines **27 implementation phases (0–26)** but **does not give approved calendar dates, cost totals or verified percentages complete**. The **16-week** schedule (9 November 2026–28 February 2027) below is an editorial example for sequencing web-MVP work; obtain team-approved estimates and milestones before calling it a committed release plan. Flutter mobile remains later-phase work.

## Source-confirmed phase groups

| Phase group | Original numbered steps | Major outcomes |
| :--- | :--- | :--- |
| Brand, scaffold and UI shell | 0–5 | Repo, React/TS, theme, auth shell, routing, dashboard mock UI |
| Working POS and application features | 6–10 | POS cart, inventory, customers, accounting, remaining screen areas |
| QA and static deployment | 11–13 | Unit/browser tests, GitHub Actions, Pages mock-data frontend |
| Online service foundation | 14–20 | Google Sheets data model, Apps Script API, roles, sales, reports and audits |
| Sync, mirror and hardening | 21–24 | Python job, MySQL mirror, reconciliation, monitoring |
| Owner mobile | 25–26 | Mobile requirements and Flutter owner application (later stage) |

## Illustrative 16-week MVP Gantt

```mermaid
gantt
  title Byte Buz — Proposed 16-Week Web MVP (Illustrative)
  dateFormat YYYY-MM-DD
  axisFormat %d %b
  section Foundation
  Brand and existing repo audit :2026-11-09, 7d
  React/TS shell and reusable UI :2026-11-16, 14d
  Dashboard UI with mock data :2026-11-30, 14d
  section Functional UX
  Cashier POS with cart logic :2026-12-14, 14d
  Inventory, supplier and CRM screens :2026-12-28, 21d
  Accounting, branches and reports screens :2027-01-11, 21d
  section Data services
  Sheets model and Apps Script foundation :2027-01-18, 14d
  Permissions, POS writes and audit events :2027-02-01, 14d
  section Verification & operations
  Browser tests, QA and secure demo :2027-02-08, 14d
  Python to MySQL mirror prototype :2027-02-08, 14d
  Pilot evaluation and written handover :2027-02-22, 7d
```

**The dates above are suggested, not taken from the original source or verified development status.** The chart intentionally allows overlap; workload and resources have not been validated. It is not a promise of a production payment system.

## Milestone gates

| Gate | Evidence needed | Current public status |
| :--- | :--- | :--- |
| G1 · Visual foundation | Dashboard renders and is compared with reference | Not verified here |
| G2 · Safe POS demonstration | Cart logic, tax/discount calculations, duplicate-sale tests | Not verified here |
| G3 · Core business modules | Inventory, purchases, customers and staff journeys tested | Not verified here |
| G4 · Initial authorized API | Auth, role/branch permissions and backend-validation tests | Not verified here |
| G5 · Data mirror | Python sync checkpoints and MySQL upserts reconciled | Not verified here |
| G6 · Owner review | Product walkthrough, risks, documentation and pilot sign-off | Not verified here |

## Core dependencies

```mermaid
flowchart TD
 A["Design system + frontend"] --> B["POS mock calculations"]
 B --> C["Apps Script rules + auth"]
 C --> D["Sheets-authoritative sale processing"]
 D --> E["Python incremental sync"]
 E --> F["MySQL mirror"]
 C --> G["Security tests / permissions"]
 G --> H["Owner pilot readiness"]
 F --> H
```

## Release principles

Never treat screenshots as an implemented system, fake data as business figures, or a mirror as a second authoritative ledger. Preserve protected source repos and consult the owner before changing business calculations, stored data, permissions or payment behavior.

[← Project home](./README.md)
