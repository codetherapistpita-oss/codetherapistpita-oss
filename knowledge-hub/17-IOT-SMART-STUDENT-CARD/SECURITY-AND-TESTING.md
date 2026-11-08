# 🔐 KIU OneCard — Security, Privacy & Prototype Testing Plan

[← Project homepage](./README.md) · [Architecture](./ARCHITECTURE.md) · [Gantt](./GANTT-CHART.md)

## Prototype boundary

Use only **fictional or consented test records**, isolated lab Wi-Fi, protected service credentials and safe devices. The university's actual financial, student and access-control databases are **out of scope** absent written authorization.

## Threats and controls

| Risk | Required control or treatment |
|---|---|
| Copied NFC identifier | Demonstration UID cannot be trusted as secure authentication; choose challenge-response smart-card technology before deployment |
| Compromised terminal | Per-device credentials and revocation; avoid one hard-coded shared secret |
| Exposed API responses | Return only minimal service decisions; enforce server-side role checks |
| Insecure network traffic | TLS with certificate validation; no disabled verification |
| Replay/duplicate requests | Fresh request ID, expiry/replay checks and idempotent processing |
| Lost or stolen student card | Immediate deactivation and controlled replacement workflow |
| Sensitive audit logs | Access control, limited retention, integrity protection and audit access review |
| Offline connectivity | Deny sensitive authorizations rather than assuming clearance |
| Optional biometrics | Explicit consent, data minimization and approved processing plan |

## Proposed acceptance tests

| ID | Test | Expected behavior |
|---|---|---|
| T01 | Valid card at identity terminal | VERIFICATION outcome recorded |
| T02 | Valid library-eligible card | ELIGIBLE, no finance attributes shown |
| T03 | Unpaid simulated finance account | PENDING; no exposure of balance |
| T04 | Exam not registered | NOT ELIGIBLE / MANUAL REVIEW |
| T05 | Unknown card | Denied with generic safe message |
| T06 | Revoked/lost card | Denied across all four terminals |
| T07 | Library terminal attempts finance service | Server rejects unauthorized scope |
| T08 | Wi-Fi disconnected | No false success, clear retry message |
| T09 | Simultaneous repeated scans | Bounded handling, auditable decision |
| T10 | Tampered/replayed request | Request rejected or flagged |
| T11 | Wrong terminal certificate/credential | Terminal rejected |
| T12 | Incorrect student identity match | Manual review escalation |

## Evaluation plan (not yet measured)

| Metric | Measurement method | Suggested target for planning |
|---|---|---|
| Scan-to-decision latency | Timestamp start/end for 30–50 scans per terminal | Report median and p95; agree threshold with supervisor |
| Verification accuracy | Known labeled test profiles | 100% correct demo decisions on curated tests |
| Unauthorized access prevention | Negative authorization tests | 0 unauthorized successful responses |
| Availability | Successful scans over total attempts | Record uptime and failure causes |
| Usability | Observed user test script | Record clarity, errors and feedback |
| Reliability | Repeated card reads | Log failures and retry counts |

**Targets are proposed acceptance criteria, not achieved results.** Collect raw observations and report uncertainty transparently.

## Documentation deliverables

- Versioned firmware, API and schema design specifications (no secrets).
- Prototype assembly drawings and connection tests.
- Photos of permitted demonstration devices.
- Sanitized test dataset and repeatable test instructions.
- Test results, defect log and corrections.
- Final report and presentation slides.

## Security resources

- [Espressif — ESP32 security overview](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/security.html)
- [OWASP — API Security Top 10](https://api-security.owasp.org/editions/2023/en/0x11-t10/)
- [NIST — Cybersecurity Framework](https://www.nist.gov/cyberframework)

[← Project homepage](./README.md)
