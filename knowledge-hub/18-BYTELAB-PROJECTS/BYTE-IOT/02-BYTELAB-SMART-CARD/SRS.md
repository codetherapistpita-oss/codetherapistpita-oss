# ByteLab Smart Card — Software Requirements Specification

## Scope
Create a branded NFC PVC card that launches an official ByteLab mobile landing page.

## Functional requirements
| ID | Requirement |
|---|---|
| FR-01 | The physical card shall carry ByteLab-approved visual branding. |
| FR-02 | The NFC chip shall store a controlled HTTPS URL using NDEF where supported. |
| FR-03 | The page shall expose the official website, services, projects and approved contacts. |
| FR-04 | Page content shall be updateable without replacing the card. |
| FR-05 | The system shall provide a QR fallback. |
| FR-06 | The page shall clearly distinguish official company links from third-party links. |

## Non-functional requirements
Mobile-first UI, fast loading, HTTPS, readable branding, minimal data on the card and no secrets stored in NFC memory.

## Future extension
A later version may pair the public profile with authenticated DESFire applications for staff identity or controlled access, but that is outside the first public-info prototype.
