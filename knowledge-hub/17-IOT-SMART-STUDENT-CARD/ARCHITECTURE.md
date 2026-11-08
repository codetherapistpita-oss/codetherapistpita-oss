# 🏗️ KIU OneCard — System Architecture & Data Flow

[← Project homepage](./README.md) · [Service terminals](./SERVICE-TERMINALS.md) · [Security plan](./SECURITY-AND-TESTING.md)

## 1. Five-layer architecture

| Layer | Components | Responsibility |
|---|---|---|
| **1 · Card** | RFID/NFC card or test tag | Presents a prototype credential |
| **2 · Edge device** | PN532 + ESP32 + OLED + LEDs/buzzer | Reads credential, makes authenticated service request, displays outcome |
| **3 · Connectivity** | Authorized Wi-Fi / local LAN, HTTPS | Provides protected communication |
| **4 · Application** | Central API + service modules + database | Resolves identity, enforces permissions, returns minimal decision |
| **5 · Observability** | Event log, audit interface, test dashboard | Records outcome and supports diagnostics |

```mermaid
flowchart TB
 subgraph Student["Physical layer"]
  CARD["Test smart card"]
 end
 subgraph Terminals["Edge / IoT terminals"]
  ID["Identity · ESP32 + PN532"]
  LIB["Library · ESP32 + PN532"]
  EX["Examination · ESP32 + PN532"]
  FIN["Finance · ESP32 + PN532"]
 end
 subgraph Backend["Prototype network & central server"]
  API["HTTPS API gateway"]
  AUTH["Terminal authentication + role authorization"]
  SERVICE["Service-specific decision engine"]
  DB[("Sample student + service records")]
  AUDIT[("Append-only audit events")]
 end
 CARD --> ID
 CARD --> LIB
 CARD --> EX
 CARD --> FIN
 ID --> API
 LIB --> API
 EX --> API
 FIN --> API
 API --> AUTH --> SERVICE
 SERVICE <--> DB
 SERVICE --> AUDIT
 SERVICE --> API
```

## 2. Scan-to-response sequence

```mermaid
sequenceDiagram
  actor Student
  participant Card as Test NFC Card
  participant Reader as PN532 + ESP32
  participant API as Central API
  participant DB as Demo Database
  participant Audit as Audit Log
  Student->>Reader: Tap card
  Reader->>Card: Detect credential
  Card-->>Reader: Prototype card reference
  Reader->>API: HTTPS verification request + terminal identity
  API->>API: Authenticate device and authorize service
  API->>DB: Resolve credential and check service rule
  DB-->>API: Relevant status only
  API->>Audit: Record time, terminal, action and outcome
  API-->>Reader: Minimal decision (no unnecessary student data)
  Reader-->>Student: OLED/LED result
```

## 3. Central data design (conceptual)

```mermaid
erDiagram
  STUDENT ||--o{ CARD : assigned
  STUDENT ||--o{ SERVICE_STATUS : has
  SERVICE_POINT ||--o{ AUDIT_EVENT : produces
  STUDENT ||--o{ AUDIT_EVENT : referenced
  CARD ||--o{ AUDIT_EVENT : presented
  STUDENT {
    uuid id PK
    string display_name
    string student_status
  }
  CARD {
    uuid id PK
    uuid student_id FK
    string credential_reference
    string card_state
  }
  SERVICE_POINT {
    uuid id PK
    string service_type
    string terminal_identity
    string active_state
  }
  SERVICE_STATUS {
    uuid student_id FK
    string service_type
    string decision_status
    datetime updated_at
  }
  AUDIT_EVENT {
    uuid id PK
    uuid service_point_id FK
    string outcome
    datetime event_time
  }
```

*Only sanitized sample records belong in any public demo. A real system requires retention rules, encryption, appropriate institution policies, and reviewed schema design.*

## 4. Example interface contract (illustrative, not deployed)

Proposed request:

```http
POST /api/v1/terminal/verify
Content-Type: application/json
Authorization: Bearer <DEVICE_CREDENTIAL>

{
  "card_reference": "TEST-CARD-0007",
  "service": "library",
  "request_id": "demo-req-0042"
}
```

Example response:

```json
{
  "request_id": "demo-req-0042",
  "decision": "ELIGIBLE",
  "message": "Library access approved",
  "timestamp": "2026-11-09T10:00:00Z"
}
```

These examples use **fictional identifiers**. In a deployed system, the API must derive permitted service from the authenticated terminal identity, not blindly trust an arbitrary `service` field. Include request freshness, rate limiting and audit correlation. Do not place shared secrets in a public firmware repository.

## 5. Security distinction: NFC UID is not proof of identity

A **UID-only** demo can be used to illustrate reading and lookup, but cannot reliably resist copying or impersonation. A real deployment needs cryptographically authenticated credentials, secure enrollment, revocation, and anti-replay controls. The physical card should not contain finance balances, grades, or extensive personal information.

## 6. Failure handling

| Failure | Desired behavior |
|---|---|
| Unknown card | DENIED / request assistance; do not disclose identity |
| Lost or blocked card | REVOKED; no service authorization |
| Network unavailable | FAIL CLOSED for access decisions; show temporary service issue |
| API timeout | Retry within bounded limits, prevent duplicate writes |
| Terminal not authenticated | Reject request; audit attempt |
| Database unavailable | No false “CLEARED” result; surface service unavailable |

## 7. Interface references

- [ESP32 security and TLS](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/security.html)
- [Adafruit PN532 SPI/I²C interface library](https://github.com/adafruit/Adafruit-PN532)
- [OWASP API object-level authorization](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/)

[← Project homepage](./README.md)
