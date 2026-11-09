# 🖼️ Knowledge Hub Image Health Report

**Date:** 9 November 2026 · **Scope:** Code Therapist public profile repository `codetherapistpita-oss/codetherapistpita-oss`, plus README/Markdown image links in the other **11 public repositories** accessible to this GitHub account.

[← Main Knowledge Hub](./README.md) · [← GitHub profile](../README.md)

## Findings

The initial Knowledge Hub repository tree had **278 Markdown documents and 57 SVG graphics**. Since the image repair work, additional preview graphics and a continuous-validation script have been committed.

| Finding | Count | Resolution |
|---|---:|---|
| Missing local PNG references — Byte Buz visual gallery | **8** | Replaced broken HTML image references with **working, labeled SVG guide cards** |
| Missing local PNG references — ByteRent visual gallery | **8** | Replaced with working labeled SVG guide cards and existing public vector logo previews |
| Missing local PNG references — Binance research gallery | **3** | Replaced broken paths with an attributed, linked original YouTube preview |
| Invalid SVG XML found during audit | **2** | Fixed unescaped ampersands in AI Academy cover and Season 03 banner |
| Dynamic external profile header | **1** | Replaced with a **repository-hosted SVG banner** |
| Missing local README image links in other public repositories | **0 found** | All local Markdown image references checked in those repository README files resolved at audit time |

**Result:** The three identified project gallery pages now contain **zero missing local image paths**. The original screenshots have **not been misrepresented as uploaded**.

## What is still pending?

The original screenshot binary files are **not yet present in GitHub**, although the owner supplied the images in conversation. These include the 8 Byte Buz PNGs, 8 ByteRent PNGs and 3 Financial News Network screenshots.

| Project | Exact original-file upload location | Instructions |
|---|---|---|
| [Byte Buz](./18-BYTELAB-PROJECTS/BYTE-BUZ/DESIGN-SHOWCASE.md) | [`assets/original/`](./18-BYTELAB-PROJECTS/BYTE-BUZ/assets/original/README.md) | [Upload guide](./18-BYTELAB-PROJECTS/BYTE-BUZ/assets/UPLOAD-GUIDE.md) |
| [ByteRent Uganda](./18-BYTELAB-PROJECTS/BYTERENT-UGANDA/DESIGN-SHOWCASE.md) | [`assets/original/`](./18-BYTELAB-PROJECTS/BYTERENT-UGANDA/assets/original/README.md) | [Original asset manifest](./18-BYTELAB-PROJECTS/BYTERENT-UGANDA/assets/ORIGINAL-IMAGES-UPLOAD.md) |
| [Binance heist](./10-CYBER-INCIDENTS-AND-LAW/CRYPTO-AND-EXCHANGE-HEISTS/BINANCE-2026-10-29/README.md) | [`assets/original/`](./10-CYBER-INCIDENTS-AND-LAW/CRYPTO-AND-EXCHANGE-HEISTS/BINANCE-2026-10-29/assets/original/README.md) | [Screenshot manifest](./10-CYBER-INCIDENTS-AND-LAW/CRYPTO-AND-EXCHANGE-HEISTS/BINANCE-2026-10-29/assets/SCREENSHOT-UPLOAD.md) |

Once these PNGs are committed, the gallery pages can switch from labeled guide cards to the exact original screenshots.

## Automated quality checks

[**Image validation script**](../.github/scripts/check_markdown_images.py) and [**GitHub Actions workflow**](../.github/workflows/check-markdown-images.yml) are now committed. They check:

1. That relative image links in Markdown actually point to committed files.
2. That referenced files are nonempty.
3. That all committed SVGs are well-formed XML.
4. That repository updates do not silently introduce broken image references.

**Limitations:** These checks do not guarantee that third-party image hosts are online, that copyrighted screenshots are licensed for public redistribution, or that images look correct at every viewport. The 11 other public repositories were audited for Markdown image references, not every image loaded by their application HTML/CSS. Private applications were left untouched.

## Reader-friendly rule

Never include an image `src` that targets an uncommitted PNG or SVG. For a not-yet-uploaded asset, show a **clearly labeled existing graphic** or a textual link, and do not present a reconstruction as the exact original.

---

Code Therapist · ByteLab Uganda Ltd · Updated 9 November 2026
