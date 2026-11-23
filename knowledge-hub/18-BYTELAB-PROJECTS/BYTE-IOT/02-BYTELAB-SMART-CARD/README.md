<div align="center">

# 💳 IoT Project 02 — ByteLab Smart Card
### One physical ByteLab card · One controlled digital company entry point

</div>

## Executive summary

**ByteLab Smart Card** is a printable NFC PVC card carrying ByteLab branding. A phone tap opens a controlled ByteLab landing page containing the company website, services, projects, verified contact channels and other approved public resources.

For a simple phone-tap web card, the preferred chip family is **NDEF-capable NTAG21x**. A DESFire-class card is justified only when the project expands into authenticated access or protected applications.

```mermaid
flowchart LR
  CARD["💳 ByteLab NFC PVC Card"] --> PHONE["📱 Phone"]
  PHONE --> PAGE["🌐 ByteLab Smart Page"]
  PAGE --> WEB["Website"]
  PAGE --> SERVICES["Services"]
  PAGE --> PROJECTS["Projects"]
  PAGE --> CONTACT["Contact / WhatsApp"]
```

## Documentation
- [SRS](./SRS.md)
- [Architecture & Workflow](./ARCHITECTURE.md)
- [Gantt](./GANTT.md)
- [Quotation](./QUOTATION.md)

[← Byte IoT family](../README.md)
