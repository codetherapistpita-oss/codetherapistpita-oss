# Image-first publishing standard

**Effective:** 11 November 2026 · **Applies to:** Code Therapist Knowledge Hub, profile cards, topic pages, and future daily concepts.

## Core rule
Every new concept must have an informative, relevant, sharp image. **Do not replace missing images with plain colored-background cards.** For Python, show actual Python code, a developer workspace, or a clear explanatory diagram; similarly match all other subjects. Images must help teach the concept, not merely decorate it.

## Visual specification
- Prefer 16:9 HD landscape for article headers; adapt to actual target component ratios with subject-aware crops. Preserve the original image and use derived crops when multiple sizes are required.
- Use genuine high-resolution photography, accurately labelled technical diagrams, or original illustrations. Avoid fake screenshots, illegible code, random stock imagery, distorted logos, and misleading AI-generated depictions.
- Balanced lighting, readable subject, sensible contrast, restrained overlay text, descriptive alt text, and mobile-safe composition.
- No generic colored placeholder cards, white rounded corners baked into imagery, stretched or half-loaded banners, excessive blur, or quality loss from repeated resizing.
- Use animation selectively and offer a static fallback; avoid distracting loops.
- Attribute third-party images and verify permitted usage rights and source URLs. Do not assume every downloaded image may be republished.

## Publication checklist
1. Inspect existing article, category and assets; prevent duplicates.
2. Choose or create a topic-specific visual and verify its license or provenance.
3. Prepare image at intended landscape aspect ratio, preserve HD, optimize file size, and save under a stable assets path.
4. Commit the actual image bytes before referencing it in Markdown; verify case-sensitive relative paths and meaningful alt text.
5. Verify GitHub article rendering, profile card display and mobile crop; fix failures before marking complete.
6. Log image path, source/license, dimensions, article URL, commit and verification result in the daily handover document.
7. Maintain the pending ~400-image inventory/ZIP task separately. Count actual files and package 50 per archive; do not claim that archives exist until generated and checked.

## Existing content migration
The fifteen concept briefs published on 11 November 2026 are awaiting informative visuals. Upgrade them without deleting their text. Do not mark their images as complete until uploaded and tested.

## Design principle
**The image should explain or demonstrate the subject.** Layout color may support readability, but it must never substitute for the subject image.
