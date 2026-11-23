# ByteLab Smart Card — Architecture & Workflow

```mermaid
flowchart TD
  A["Printable NFC PVC card"] --> B["NFC phone"]
  B --> C["HTTPS ByteLab landing page"]
  C --> D["Company website"]
  C --> E["Products and projects"]
  C --> F["WhatsApp / contact"]
  C --> G["Social / developer links"]
  H["ByteLab content owner"] --> C
```

## Card-data rule
Store only the URL and minimal metadata needed for the tap experience. The company page remains the source of truth.

## Chip guidance
- **Public web-card use:** NTAG213/215/216 or equivalent NDEF-capable NFC Forum tag.
- **Protected access use:** DESFire-class credential with server-side authorization.
