# 01 · Product Brief, Scope & Roles

[← Project home](./README.md) · [Features](./FEATURES-AND-SCREENS.md) · [Architecture](./SYSTEM-ARCHITECTURE.md)

> **Source basis:** Byte Buz AI Coding Master Prompt **v1.0** (previously prepared by the owner). Public summary only; not a new or replacement private SRS.

## Product identity

| Field | Confirmed design decision |
| :--- | :--- |
| Product | **Byte Buz** (not Byte Buzz, ByteBiz or ByteBus) |
| Company | ByteLab Uganda Ltd |
| Identity | Code Therapist / Gyagenda Peter Katabalwa |
| Initial market | Uganda; long-term ambitions beyond Uganda |
| Primary application | Business management and web POS |
| Later mobile target | Owner-focused Flutter application |
| Brand treatment | Deep blue navigation, white content, controlled modern red |

## Business requirements at a glance

The source defines a platform bringing together **sales, inventory, suppliers, customers, accounting, staff, loyalty, analytics, branch oversight, reports, audits, business-day management and synchronization**. The initial product is **online-first**; a fully offline POS experience is not yet a confirmed shipped capability.

### Primary personas

| Role | Proposed capabilities |
| :--- | :--- |
| Business Owner | Business-wide financial and operational visibility |
| Administrator | Day-to-day setup, products, staff, stock and configuration |
| Branch Manager | Branch-specific oversight, approvals and business-day closure |
| Accountant | Expenses, reconciliation, reports and cash flow |
| Cashier | POS transactions, approved discounts and receipts |
| Stock Officer | Receipts, inventory adjustments and transfers |
| Auditor | Authorized read-only reports, audit events and exceptions |
| Customer Care | Customer requests within permitted access |
| Platform Super Admin | Later platform-level account administration |

**Authorization rule:** A visible menu is not a security boundary. Sensitive actions require validated **backend permission checks**, an identified user and an audit record.

## UX design principles

- Desktop-first management dashboard, adapted for tablets and touch-friendly cashier use.
- White content panels, compact readable figures, blue information controls and red warnings.
- Shared navigation, data tables, charts and forms rather than recreated static screenshot widgets.
- Actual charts must be derived from system data; screenshots are **references only**.
- Strong empty, loading, success, failure and permission-denied states.
- Screens must not report fictitious activity as live metrics.

## Scope distinctions

**Source-confirmed design:** 20 screen/page definitions, POS rules, Sheets/Apps Script initial backend, Python→MySQL mirror, extensive permissions and future Flutter owner app.

**Not source-confirmed as delivered:** launched production SaaS, running payment integrations, active accounting automation, real branch metrics, approved licensing or individual commercial deadlines.

## Public boundaries

The public showcase must not expose authentication secrets, production spreadsheet IDs, private customer/supplier records, proprietary instructions, private source code, signed commercial documents or actual business performance without explicit authorization.

[← Project home](./README.md)
