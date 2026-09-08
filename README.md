# Agentic AI Job Application & Career Automation Platform

> **Status📋: In Development (Work in Progress)**
> This project is under active construction. Core architecture and several milestones are being built incrementally — it is **not yet feature-complete or production-ready**. See the [Development Roadmap](#-development-roadmap--milestones) below for current progress.

---

## 📌 Overview

This project is a **production-grade Agentic AI Job Application Platform** that autonomously discovers relevant job opportunities based on a user's resume/profile, analyzes and ranks those opportunities, prepares tailored application materials, navigates supported job portals, fills out application forms, answers application questions, and requests **human approval via SMS** before submitting any application on the user's behalf.

The system is intentionally **not** a simple chatbot, scraper, or one-off automation script. It is designed as a serious agentic system combining:

- Modular AI agents
- Deterministic state management
- Browser automation
- Persistent storage
- Human-in-the-loop approval
- Observability & error handling
- A scalable, extensible architecture

---

## Primary Objective

Given a user's resume and profile as the single source of truth, the platform will:

1. Discover jobs matching the candidate's profile
2. Analyze and structure each job description
3. Calculate a job-to-candidate match score
4. Analyze the resume against job requirements
5. Generate tailored cover letters / application messages
6. Navigate supported job portals and fill out application forms
7. Answer application questions using verified profile data
8. Send an **SMS approval request** before submission
9. Submit the application **only after explicit human approval**
10. Track every application and surface it on a live dashboard

---

## Core Principle: Human-in-the-Loop

The AI is allowed to autonomously discover, analyze, score, prepare, and fill out applications — but it will **never submit an application without explicit human approval**.

```
Job Discovery → Job Analysis → Match Score → Resume Analysis
     → Application Preparation → Form Filling → Question Answering
     → SMS Approval Request → [User Approves?]
                                    ├── YES → Submit → Track
                                    └── NO  → Stop / Reject
```

There is **no path** from application preparation directly to submission without a human-approved checkpoint.

---

## System Capabilities (Planned)

| Area | Description |
|---|---|
| **Resume & Profile Management** | Structured extraction of skills, experience, education, certifications, and preferences — no fabricated data, ever. |
| **Job Discovery Agent** | Modular, source-agnostic job discovery (job boards, ATS platforms, career pages), normalized into a common schema. |
| **Job Analysis Agent** | Structured parsing of requirements into Required / Preferred / Optional categories. |
| **Match Score Engine** | Configurable, explainable 0–100 scoring engine (skills, experience, education, role relevance, etc.). |
| **Resume Analysis Agent** | Honest gap analysis — matching skills vs. missing skills, without inflating the score. |
| **Tailoring & Cover Letter Agents** | Job-specific resumes, cover letters, and messages generated from real candidate data only. |
| **Application Agent** | Playwright-based browser automation with adapters per platform (Workday, Greenhouse, Lever, generic sites). |
| **Question Answering Agent** | Classifies questions into safe-to-automate, reasoning-required, and human-confirmation-required categories. |
| **SMS Approval System** | Secure, expiring approval links sent via SMS before any submission occurs. |
| **Submission Agent** | Submits only after verified approval, and confirms actual submission before marking as complete. |
| **Application Tracking** | Full lifecycle tracking via a deterministic state machine (Discovered → Applied → Interview → Offer, etc.). |
| **Dashboard** | Web dashboard for search, filtering, analytics, and per-application detail views. |

---

## High-Level Architecture

```
                    ┌───────────────────┐
                    │   Candidate Data  │
                    │ (Resume / Profile)│
                    └─────────┬─────────┘
                              ▼
        ┌───────────────────────────────────────────┐
        │              Agent Orchestration          │
        │              (LangGraph, stateful)        │
        └───────────────────────────────────────────┘
     Discovery → Analysis → Matching → Resume Analysis
     → Prep → Form Fill → Question Answering
     → SMS Approval (Human-in-the-Loop) → Submission → Tracking
                              │
                              ▼
                    ┌───────────────────┐
                    │   Web Dashboard   │
                    └───────────────────┘
```

Design philosophy: **use AI where reasoning is required, and deterministic software everywhere else** (database ops, scoring math, state transitions, approval validation, form logic).

---

## Recommended Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Next.js, React, TypeScript, Tailwind CSS |
| **Backend** | Python, FastAPI |
| **Agent Orchestration** | LangGraph |
| **Browser Automation** | Playwright |
| **Database** | PostgreSQL + pgvector (for embeddings/RAG) |
| **Background Processing** | Redis + Celery / RQ |
| **Object Storage** | S3-compatible storage (resumes, generated docs, artifacts) |
| **Deployment** | Docker, AWS, CI/CD |

---

## Security & Safety Principles

- No fabricated resume/experience data — ever.
- No sensitive application questions (e.g., legal declarations, sponsorship, background checks) are auto-answered without human confirmation.
- No submission occurs without an explicit, verified **APPROVED** state.
- No plaintext storage of job-portal credentials; secrets are never passed to the LLM.
- Secure, expiring, single-use approval tokens (no guessable URLs).
- Audit logging, rate limiting, and no sensitive data in logs.

---

## Application State Machine

```
DISCOVERED → ANALYZING → MATCHED → PREPARING → AWAITING_APPROVAL
     → APPROVED → SUBMITTING → APPLIED → INTERVIEW → OFFER
                              ↘ REJECTED / FAILED / WITHDRAWN
```

Invalid transitions (e.g., `PREPARING → APPLIED` without approval) are structurally disallowed.

---

## Testing Strategy (Planned)

- **Unit tests** — match scoring, resume parsing, job normalization, state transitions, duplicate detection
- **Integration tests** — database, AI services, SMS provider, storage, browser automation
- **Browser tests** — mock/demo application forms first; real portals only after the workflow is proven reliable

---

## Human Override

At every stage, the human user can override the AI:

- Apply to a job the AI recommended rejecting (or vice versa)
- Edit any AI-generated answer or cover letter before approval
- Reject any application regardless of match score

---

## Disclaimer

This is a personal/academic engineering project exploring agentic AI system design, human-in-the-loop workflows, and browser automation. It is currently **incomplete and evolving** — architecture, folder structure, and feature scope are subject to change as development progresses.
