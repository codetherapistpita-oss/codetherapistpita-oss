# 🏗️ ByteRent — Proposed System Architecture

[← Project home](./README.md) · [Security & quality](./TRUST-AND-QUALITY.md)

## Stage 1 · Controlled pilot

The proposal and SRS describe a limited user-validation stage:

```mermaid
flowchart TD
 APP["Flutter / Dart prototype"]
 AUTH["Firebase Authentication (where appropriate)"]
 API["Google Apps Script endpoints"]
 SHEET[("Structured Google Sheets pilot records")]
 DRIVE[("Google Drive approved pilot media")]
 APP --> AUTH
 APP --> API
 API --> SHEET
 API --> DRIVE
```

**Boundary:** This is for **small approved pilot use**, not high-volume operation, unrestricted document storage or a durable financial ledger.

## Stage 2 · Proposed full production

```mermaid
flowchart TB
 MOBILE["Flutter client"]
 NODE["Node.js API / business workflows"]
 PY["Python: selected analytics, automation and recommendations"]
 SQL[("MySQL relational data")]
 MEDIA[("Protected object / media storage")]
 EXT["Approved maps, communication and payment providers"]
 MON["Monitoring, audit, backups and recovery"]
 MOBILE -->|"TLS / authenticated requests"| NODE
 NODE --> SQL
 NODE --> MEDIA
 NODE --> EXT
 NODE <--> PY
 NODE --> MON
```

Production requires protected service authorization, durable data, media access controls, proper transaction states, recovery exercises and capacity planning. No specific payment, hosting or maps vendor is asserted as already contracted.

## Role and authorization boundaries

```mermaid
flowchart LR
 A[Authenticated user] --> B{Access policy}
 B -->|Seeker| C[Own favourites, enquiries, applications]
 B -->|Provider| D[Authorized listings and related requests]
 B -->|Operations| E[Assigned moderation / verification / finance]
 B -->|Auditor| F[Read-only approved audit]
 B -->|Technical| G[Approved deployment and support]
```

**Authentication is not authorization.** The service must check role, organization and record ownership on each protected operation. Staff should use named accounts and least privilege.

## Proposed high-level data entities

| Entity | Purpose |
|---|---|
| User & provider organization | Identity, approved role, contact/preferences |
| Property listing | Type, location, fees, owner/provider reference and state |
| Listing media | Approved photographs and evidence status |
| Availability | Date/rental availability and booking constraints |
| Enquiry / appointment | Questions, viewing slots and status |
| Application / booking | Documented action with state transitions |
| Payment transaction | Approved provider reference, receipt and reconciliation state |
| Verification / fraud case | Evidence review, moderation, outcomes |
| Audit event | Security-sensitive action and actor/time |

This table is an **explanatory summary of the requirements**, not the complete confidential production schema.

## Migration concept

```mermaid
flowchart LR
 A[Pilot validation] --> B[Approved baseline and mapping]
 B --> C[Sanitized export and cleanup]
 C --> D[Import into production system]
 D --> E[Reconciliation, rollback rehearsal]
 E --> F[Authorized production go/no-go]
```

The production service and its data model supersede Apps Script/Sheets for authoritative national operations; stable identities and documented interfaces support migration.

[← Project home](./README.md)
