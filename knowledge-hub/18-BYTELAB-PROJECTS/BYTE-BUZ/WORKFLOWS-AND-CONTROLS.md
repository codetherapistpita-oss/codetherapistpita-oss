# 04 · Operational Workflows & Business Controls

[← Project home](./README.md) · [Technology](./SYSTEM-ARCHITECTURE.md) · [Designs](./DESIGN-SHOWCASE.md)

## Sale → Stock → Payment → Receipt

```mermaid
flowchart TD
 A["Cashier opens till & selects branch"] --> B["Scan barcode / search product"]
 B --> C["Validate stock, price and discounts"]
 C --> D["Calculate totals on API"]
 D --> E{"Payment confirmed?"}
 E -->|No| F["Hold or cancel without stock deduction"]
 E -->|Yes| G["Commit sale, payment and stock movements"]
 G --> H["Issue unique receipt"]
 H --> I["Add audit event + feed analytics"]
```

**Protection:** Unique sale ID and idempotency key, server-side stock checks, safe money arithmetic and recorded cancellation/refund operations.

## Supplier → Purchase Order → Goods Receipt

```mermaid
flowchart LR
 A["Supplier selected"] --> B["Purchase order"]
 B --> C["Approval / expected delivery"]
 C --> D["Receive stock + verify quantity"]
 D --> E["Stock movement + payable"]
 E --> F["Payment and reconciliation"]
```

Changes to stock must be traceable: receipts add inventory; sales subtract it; transfers produce an outflow at the source branch and an inflow at the destination; adjustments require reasons.

## Branch management and stock redistribution

```mermaid
flowchart TD
 A["Compare branch quantities"] --> B{"Below reorder level?"}
 B -->|Yes| C["Review transfer / purchase suggestion"]
 B -->|No| D["Continue monitoring"]
 C --> E["Manager-authorized transfer"]
 E --> F["Source out / target in"]
 F --> G["Audit both movement references"]
```

Recommendations are support for a manager, not an autonomous transfer of stock.

## Daily till control

```mermaid
flowchart TD
 A["Opening float + cashier assignment"] --> B["Register sales / cash movements"]
 B --> C["End of shift — count cash"]
 C --> D["Compare expected vs counted"]
 D --> E{"Variance above policy?"}
 E -->|Yes| F["Investigate and request approval"]
 E -->|No| G["Manager reviews closure"]
 F --> G
 G --> H["Close business day and retain evidence"]
```

Cash variances and exceptions must remain in the accounting and audit records. The mock screen's sample sales/cash numbers are not real transactions.

## Customer rewards and promotions

Marketing consent is separately recorded. Campaigns set an approved audience, eligible products, date window, discount limits, redemption policy and responsible approver. All discounts are recorded against relevant sales for reporting.

## Control matrix

| Control | Required business behavior |
| :--- | :--- |
| Price override | Authorized role, reason, previous/current value, audit event |
| Refund | Original receipt link, condition, approval threshold, reversal record |
| Stock adjustment | Reason, branch, user, signed movement and audit |
| Manual sync | Privileged action with job ID, time and outcome |
| Backup restore | Owner-approved and logged |
| Supplier suspension | Role check, rationale and status history |

[← Project home](./README.md)
