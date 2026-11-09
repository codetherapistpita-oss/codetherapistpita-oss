# 🤖 Gemini — AI Family Study Profile

**Developer:** Google DeepMind / Google · **Origins:** 2023 · **Profile reviewed:** 9 November 2026

[← 15-model catalog](../MODEL-CATALOG.md) · [← AI Academy](../README.md)

> **Important distinction:** Proprietary multimodal model family and app. A consumer chatbot, underlying model, API and open-weight distribution are not necessarily the same product. Avoid comparing model families by marketing claims alone.

## 1. Where this AI came from

Google announced the first Gemini family on 6 December 2023, emphasizing multimodal understanding. [Official background](https://blog.google/innovation-and-ai/technology/ai/google-gemini-ai/).

## 2. What it does

**Typical applications:** Text, images, coding, media analysis and Google workflows.

**Current research note:** Google DeepMind's model-card index covers newer Gemini versions, including 2026 models; check exact release/model card dates. This page summarizes a model **family**; it does not claim a single version is universally best or list unsupported prices and benchmark rankings.

## 3. How a learner can use or investigate it

1. Open the [official entry point](https://gemini.google.com/) and check account requirements and access in your region.
2. Start with a **non-confidential** task, using a clear objective and an example.
3. Request a structured answer, assumptions, source links where available and uncertainty.
4. Check important claims against original sources; run code before trusting it.
5. Compare the result on the same task with another model family in the catalog.

**Lab exercise:** Use a public photo of a classroom (or a simple diagram you drew), ask Gemini to describe its content and identify uncertainties.

## 4. Technical questions

- Is the selected version proprietary, open-weight, or under a specific custom license?
- Is the model served online or deployable locally? What hardware and storage are required?
- Which modalities and tools does the **specific version** accept?
- What data retention, training-use, privacy and organizational settings apply?
- How are answers evaluated for factual accuracy, bias, reliability, latency and cost?

## 5. Simple architecture

```mermaid
flowchart LR
 A[Your task and context] --> B[Prompt / client]
 B --> C[Selected model and service]
 C --> D[Response / output]
 D --> E[Human verification and improvement]
 E --> A
```

## 6. Source links and future updates

- **Official product/site:** https://gemini.google.com/
- **Origin/background:** https://blog.google/innovation-and-ai/technology/ai/google-gemini-ai/
- **Release notes, cards or documentation:** https://deepmind.google/models/model-cards/

**Learning disclaimer:** Model names, availability, features, prices and default versions can change. Always check the source's own dated release notes. Product experiments should not involve real client files without approval.

### Check your understanding

1. What distinguishes the product name from its underlying model family?
2. Name two suitable applications and one unsafe assumption.
3. What would you verify before using this family for a business project?

[← AI Academy](../README.md) · [Prompt engineering](../SEASON-03/PROMPT-ENGINEERING.md)
