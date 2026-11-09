# 02 · Gold Marketplace User Journeys & Transaction Controls

[← Project home](./README.md) · [Architecture](./ARCHITECTURE.md) · [Compliance](./COMPLIANCE-AND-TRUST.md)

## A. Buyer journey

```mermaid
flowchart TD
 A["Browse public education and approved listings"] --> B["Select a seller / gold specification"]
 B --> C["Review what was actually verified"]
 C --> D["Submit enquiry and request quote"]
 D --> E["Buyer verification and lawful purpose review"]
 E --> F{"Compliance approved?"}
 F -->|No / incomplete| G["Request documents or decline case"]
 F -->|Yes| H["Independent assay / contract review"]
 H --> I{"Permits, payment and logistics approved?"}
 I -->|No| J["No checkout; remain on hold"]
 I -->|Yes| K["Approved partner transaction"]
 K --> L["Documented handover / dispute window"]
```

**Example:** A buyer in Kampala enquires about a hypothetical 100g listing. The portal **must not infer the gold exists**, is genuine or available. A trained reviewer checks counterparty documents, metal evidence, source, payment plan and transaction lawfulness before anything progresses.

## B. Seller onboarding and listing lifecycle

```mermaid
flowchart TD
 S["Seller applies"] --> ID["Business identity, owner and licences"]
 ID --> KYC["KYC, sanctions/PEP and legal review"]
 KYC --> ORIGIN["Source-of-gold and custody/provenance evidence"]
 ORIGIN --> LAB["Third-party assay and specification check"]
 LAB --> DEC{"Authorized and supported?"}
 DEC -->|No| REJ["Reject / hold with audit reason"]
 DEC -->|Yes| APPROVE["Time-limited listing approval"]
 APPROVE --> MON["Renew documents, monitor risk, resolve disputes"]
 MON -->|Expiry or issue| REJ
```

### Seller data to consider

Business legal name, registered jurisdiction, dealer/mining rights status, beneficial owners, authorization expiry, authorized signatory, contact details, gold form, quantity, purity, origin, location of custody, assay results and the chain of supporting documents. Never expose private identity documents publicly.

## C. Quote and deal status

| Stage | Meaning | Permitted action |
|---|---|---|
| Draft enquiry | A person expresses interest | No financial commitment |
| Buyer onboarding | Identity and purpose checked | Enquiry remains restricted |
| Seller document review | Evidence is under review | No “verified” public claim yet |
| Quotation | Terms proposed with validity period | Not a payment instruction by itself |
| Compliance hold | A risk or missing permit prevents progress | No settlement |
| Contract reviewed | Legal scope, quality and settlement conditions approved | Escalate to authorized partners |
| Authorized transaction | All necessary approvals explicitly recorded | Execute only through lawful approved process |
| Fulfilment / dispute | Assay acceptance, title transfer, insured delivery if applicable | Evidence and complaint handling |

## D. Human handoff and audit controls

```mermaid
sequenceDiagram
  participant B as Buyer
  participant W as Web Portal
  participant C as Compliance Reviewer
  participant S as Authorized Seller
  participant P as Regulated Settlement / Logistics Partner
  B->>W: Request quote
  W->>C: Open controlled case
  C->>S: Request seller evidence
  S-->>C: Licensing, provenance, assay and terms
  C->>C: Check buyer, seller and jurisdiction
  alt missing or prohibited
    C-->>W: Hold / reject and explain next steps
  else lawful and reviewed
    C-->>W: Permit next stage
    W-->>B: Approved quotation details
    B->>P: Complete separately approved transaction
    P-->>W: Documented status, no secrets
  end
```

## E. Fraud and dispute pathways

False assay certificates, spoofed dealer identities, stolen source documents, bait pricing, impersonated staff, attempted off-platform payments and origin inconsistencies must trigger documented investigation/holds. Support escalation to responsible law enforcement/regulators where legally required.

**Never advertise automatic escrow, guaranteed metal purity or worldwide shipment until licensed partners and procedures are actually established.**

[← Project home](./README.md)
