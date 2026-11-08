# 03 · Technical Architecture & Data Ownership

[← Project home](./README.md) · [Modules](./FEATURES-AND-SCREENS.md)

## Confirmed early-stage architecture from the owner brief

```mermaid
flowchart TB
  subgraph FE["Client and hosting"]
   WEB["React + TypeScript + Vite frontend"]
   PAGES["GitHub Pages — static hosting"]
   WEB --- PAGES
  end
  subgraph SERVICE["Online operational layer"]
   APPS["Google Apps Script — validation, permissions and API"]
   GS[("Google Sheets — initial online records")]
   APPS --> GS
  end
  subgraph MIRROR["Independent mirror and reporting"]
   PY["Python incremental synchronization"]
   MYSQL[("MySQL — one-way local mirror")]
   PY --> MYSQL
  end
  WEB -->|"Authenticated service calls"| APPS
  APPS -->|"Approved changes / sequence"| PY
```

**Important architectural separation:** Apps Script is the application logic/API layer; **Google Sheets is the initial data source of truth**, and MySQL initially provides a *one-way replica*, not a second independent writer. The product brief anticipates eventual Node.js or PHP + hosted MySQL migration after a controlled redesign of backend persistence and services.

## Financially sensitive workflow

```mermaid
sequenceDiagram
  actor Cashier
  participant Web as Web POS
  participant API as Apps Script API
  participant Sheets as Online primary records
  participant Sync as Python sync worker
  participant SQL as MySQL mirror
  Cashier->>Web: Select items, tender
  Web->>API: Submit sale with idempotency key
  API->>API: Validate permission, prices, stock and totals
  API->>Sheets: Controlled sale + stock + payment writes
  Sheets-->>API: Persisted transaction reference
  API-->>Web: Confirm receipt data / error
  API-->>Sync: Incremental changed-record cursor
  Sync->>SQL: Upsert approved records in transaction
  SQL-->>Sync: Commit or rollback
```

The sequence is an **intended design**, not proof that Google Sheets can provide database-grade atomic transactions across arbitrary writes. For the initial MVP, use Apps Script locks, idempotent operations and reconciliation to limit concurrency errors, and test failure cases. **High-volume or multi-register financial operation would require stronger persistence guarantees before production use.**

## Rules that must survive any backend migration

| Data domain | Key invariant |
| :--- | :--- |
| Sales | Unique ID, authoritative calculation, duplicate prevention |
| Inventory | Controlled movement ledger; no silent balance changes |
| Payments | Explicit settlement/refund records; accurate reconciliation |
| Roles | Per-business and per-branch permission enforcement |
| Audit | Append-oriented sensitive-action history |
| Sync | Stable IDs, checkpointed sequence, safe retry and idempotent upsert |
| Customer | Permissioned access and separate marketing consent |

## Later evolution — anticipated, not selected as active production stack

```mermaid
flowchart LR
  UI["Web UI"] --> API["Node.js or PHP services"]
  MOBILE["Flutter owner mobile"] --> API
  API --> SQL[("Hosted MySQL")]
  API --> AUDIT["Observability & protected backups"]
```

The private web/backend/mobile repositories remain outside this public technical guide. No credentials, proprietary code, or real customer data are reproduced.

[← Project home](./README.md)
