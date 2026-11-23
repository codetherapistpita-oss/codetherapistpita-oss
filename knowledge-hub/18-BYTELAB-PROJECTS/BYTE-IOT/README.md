<div align="center">

# 📡 Byte IoT — Project Family
### ByteLab Uganda Ltd · Practical connected systems, NFC and edge computing

**Project 01 · Byte IoT Tap** · **Project 02 · ByteLab Smart Card** · **Project 03 · Byte IoT Access**

</div>

> [!IMPORTANT]
> Byte IoT is a public research and prototype family. Prices are planning benchmarks, not purchase receipts. Confirm exact chip model, stock and supplier quotation before buying.

## Family purpose

Byte IoT groups ByteLab experiments that connect **physical objects to useful digital services**. The family starts with NFC identity and resource sharing, then extends into branded company credentials and local/offline access-control terminals.

| No. | Project | Core idea | Main hardware |
|---|---|---|---|
| **IoT Project 01** | **[Byte IoT Tap](./01-BYTE-IOT-TAP/README.md)** | NFC key-fob opens a personal digital hub with portfolio, WhatsApp, GitHub, CV, projects and curated resources | NDEF-capable NFC key-fob/tag |
| **IoT Project 02** | **[ByteLab Smart Card](./02-BYTELAB-SMART-CARD/README.md)** | Printable ByteLab NFC card opens the company profile, website, services and verified links | Printable NFC PVC card |
| **IoT Project 03** | **[Byte IoT Access](./03-BYTE-IOT-ACCESS/README.md)** | ESP32 + PN532 terminal validates smart credentials for lab/office access and attendance | ESP32, PN532, display, smart cards |

## Shared engineering principles

- Keep credentials minimal; store a URL or identifier, not unnecessary private data.
- Use HTTPS and server-side authorization for protected functions.
- Prefer **NDEF/NTAG21x-style tags** for simple smartphone URL launching.
- Prefer stronger authenticated credentials such as **DESFire-class cards** when access decisions require real security.
- Support local-network operation where the project requires offline resilience.
- Publish architecture, requirements, testing, limitations, Gantt and quotations transparently.

## Documentation standard

Each Byte IoT project includes a **README, SRS, architecture/workflow, Gantt roadmap and quotation**.

[← ByteLab R&D](../README.md) · [← Knowledge Hub](../../README.md)
