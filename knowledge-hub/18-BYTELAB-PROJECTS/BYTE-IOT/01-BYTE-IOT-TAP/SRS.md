# Byte IoT Tap — Software Requirements Specification

## 1. Purpose
Provide a mobile-first digital hub launched by a physical NFC tap.

## 2. Actors
- **Owner/Admin:** manages profile links and resources.
- **Visitor:** taps the NFC tag and chooses a destination.

## 3. Functional requirements
| ID | Requirement |
|---|---|
| FR-01 | The NFC tag shall contain one HTTPS URL in an NDEF record. |
| FR-02 | The landing page shall load on modern mobile browsers. |
| FR-03 | The page shall provide Portfolio, GitHub, WhatsApp, Email/Contact and Projects links. |
| FR-04 | The page shall include a categorized Useful Websites directory. |
| FR-05 | The owner shall be able to update page content without rewriting the NFC tag. |
| FR-06 | External links shall open only after a user action. |
| FR-07 | The system shall provide a fallback QR code for devices without NFC. |

## 4. Non-functional requirements
- Mobile-first, fast-loading and accessible.
- HTTPS required.
- No sensitive data stored directly on the tag.
- Clear ownership and privacy notice.
- Responsive from approximately 320 px width upward.

## 5. Acceptance criteria
A test visitor taps a verified NDEF tag, opens the hub, selects at least three destinations successfully, and sees a newly added link after the owner updates the web page without rewriting the tag.
