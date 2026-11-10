<div align="center">

<img src="./assets/FIELD-07.svg" alt="Code Therapist Containers & DevOps field 07 landscape illustration" width="760"/>

# 07 · Docker Containers vs Virtual Machines

**Field:** Containers & DevOps · **Level 02 · Developer** · **Season 01 · Day 002** · **Prepared:** 9 November 2026

[← Today's 15 Fields](./README.md) · [Knowledge Hub](../../../README.md)

</div>

> **Learning objective:** A Docker container isolates a process and its dependencies while sharing the host kernel, unlike a typical VM with a guest OS.

## 01 · Lecture and key knowledge

A Docker container isolates a process and its dependencies while sharing the host kernel, unlike a typical VM with a guest OS.

The goal is to understand the concept, identify its use and limitations, and **demonstrate it safely**. A polished example, confident answer or passing design mockup is not proof that software is correctly implemented. Use this lesson as a starting point and read the original documents cited below.

## 02 · How the process works

```mermaid
flowchart LR
 N0["Code"] --> N1
 N1["Build image"] --> N2
 N2["Run container"] --> N3
 N3["Publish port"] --> N4
 N4["View logs"] --> N5
 N5["Stop"]
```

## 03 · Practical lab — Season 01 · Day 002

Draw web frontend, API and database as separate containers, and identify where persistent data lives.

### Learning procedure

1. Read the two source references below and note the key terms.
2. State the input, expected result and a failure case before beginning.
3. Perform the exercise using a **safe fictional example** or your own permitted lab.
4. Compare what actually happened with the expected result; record any error.
5. Write a short conclusion identifying where this technique is appropriate.

## 04 · Knowledge check

1. Explain the main concept to a new learner in two sentences.
2. Give an example relevant to a Ugandan student, developer or business.
3. Draw the workflow without copying the diagram above.
4. Describe one limitation or security concern and a way to evaluate it.
5. Identify an important statement and open the original source supporting it.

**Class assessment / 10 marks:** terminology (2), example (2), completed practice evidence (3), limitations (2), source verification (1). Results are not claimed to be completed.

## 05 · Ready-to-record YouTube narration

**00:00–00:08 · Hook:** “Code Therapist, Field 07: Docker Containers vs Virtual Machines. Here's the idea you should understand today.”

**00:08–00:25 · Explanation:** “A Docker container isolates a process and its dependencies while sharing the host kernel, unlike a typical VM with a guest OS.”

**00:25–00:55 · Demonstration:** Show the safe practical lab: Draw web frontend, API and database as separate containers, and identify where persistent data lives.

**00:55–01:15 · Diagram:** Explain the flowchart stage by stage, including the important limitation.

**01:15–01:25 · Closing:** “Read the full lesson and official sources in the Code Therapist Knowledge Hub. Save and share for the next day.”

**Recording checklist:** Capture your own screen or licensed assets; test any code before saying it ran; use subtitles and clearly distinguish real facts from demonstrations.

## 06 · Original sources and reference links

- [Official/primary reference 1](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Official/primary reference 2](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/)

**Accuracy and safety:** Containers are not a substitute for patching and runtime security.

## 07 · WhatsApp / YouTube share caption

**📚 CODE THERAPIST · FIELD 07 · SEASON 01 · DAY 002**

**Docker Containers vs Virtual Machines**

Learn the key idea with a clean diagram, practical exercise, study questions and official sources.

🔗 https://github.com/codetherapistpita-oss/codetherapistpita-oss/blob/main/knowledge-hub/07-SOCIAL-MEDIA/YOUTUBE/2026-11-09-TECHNOLOGY-DAILY-15/FIELD-07-docker-containers-vs-virtual-machines.md

> **Publication status:** GitHub article and video script prepared; this is not a claim that a YouTube video has been uploaded.

[← Today's 15 posts](./README.md) · [Code Therapist](https://github.com/codetherapistpita-oss)
