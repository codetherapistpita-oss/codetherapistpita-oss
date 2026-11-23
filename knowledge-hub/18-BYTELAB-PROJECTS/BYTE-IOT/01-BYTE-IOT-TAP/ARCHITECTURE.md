# Byte IoT Tap — Architecture & Workflow

```mermaid
flowchart TD
  A["NTAG21x / NDEF key-fob"] -->|Tap| B["NFC-enabled phone"]
  B --> C["OS notification / URL prompt"]
  C -->|User opens| D["HTTPS landing page"]
  D --> E["Profile links"]
  D --> F["Projects"]
  D --> G["Useful Websites"]
  D --> H["Save Contact / CV"]
  I["Owner dashboard / source"] -->|Update content| D
```

## Data boundary
The NFC tag contains a short URL only. Profile details live on the web page. This allows content to change while the physical tag remains unchanged.

## Suggested URL model
`https://bytelabug.com/tap/peter` or a controlled equivalent.

## Security
- Do not store passwords, tokens or private identifiers on the tag.
- Use HTTPS.
- Validate outbound links.
- If analytics are added, disclose them and avoid unnecessary personal tracking.
