# Byte IoT Access — Software Requirements Specification

## Functional requirements
| ID | Requirement |
|---|---|
| FR-01 | Terminal shall read an approved NFC smart credential. |
| FR-02 | Terminal shall authenticate to the authorization service. |
| FR-03 | Service shall return ALLOW, DENY or REVIEW with minimal data. |
| FR-04 | Terminal shall support local-network operation when internet is unavailable. |
| FR-05 | Revoked credentials shall be denied after synchronization. |
| FR-06 | Every decision shall create an audit event. |
| FR-07 | OLED/LED/buzzer feedback shall be understandable without relying on color alone. |

## Security requirements
- Do not trust UID alone for a security claim.
- Use per-device credentials.
- Use HTTPS or a protected local test network.
- Use synthetic or consented identities only.
- Fail closed for sensitive decisions when authorization state is stale.
