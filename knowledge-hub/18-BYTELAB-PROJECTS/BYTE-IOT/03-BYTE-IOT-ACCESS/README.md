<div align="center">

# 🚪 IoT Project 03 — Byte IoT Access
### Smart card access and attendance for a controlled lab or office prototype

</div>

## Executive summary

**Byte IoT Access** extends the Byte IoT family from public-information NFC tags into authenticated edge computing. An ESP32 terminal uses a PN532 reader to verify a smart credential against a local or online authorization service, display a decision and record an audit event.

The first prototype is intended for an **authorized lab/office test environment**, not for bypassing or controlling third-party security systems.

```mermaid
flowchart LR
  CARD["Secure Smart Card"] --> PN["PN532"]
  PN --> ESP["ESP32 Terminal"]
  ESP --> API["Local / Online Authorization API"]
  API --> DATA[("Users + Permissions")]
  API --> ESP
  ESP --> OUT["OLED + LED + Buzzer"]
  API --> LOG[("Attendance / Audit Log")]
```

## Documentation
- [SRS](./SRS.md)
- [Architecture](./ARCHITECTURE.md)
- [Gantt](./GANTT.md)
- [Quotation](./QUOTATION.md)

[← Byte IoT family](../README.md)
