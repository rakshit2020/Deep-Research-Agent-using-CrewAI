# Deep Research Crew (CrewAI + NVIDIA NIM)

A structured **deep research system** built using **CrewAI** and **NVIDIA NIM–powered LLMs**.  
This project focuses on **clarity-first research**: it explicitly clarifies the user’s intent before planning and executing any research, ensuring the final output aligns closely with what the user actually wants.

---

## Overview

This system implements a **multi-agent research workflow** where each agent has a clearly defined responsibility:

- The workflow **starts by clarifying the user’s request** to remove ambiguity.
- Research planning is done only after requirements are locked.
- Web research is executed with enforced depth (multiple searches).
- Findings are synthesized into a professional, evidence-backed report.

The design avoids premature assumptions and produces more reliable, goal-aligned research outputs.

---

## Agents Used

- **Research Manager**
  - Engages with the user to clarify scope, depth, constraints, and expectations.
  - Ensures ambiguity is removed before research begins.
  - Creates a structured research plan aligned with the clarified requirements.

- **Deep Researcher**
  - Executes the research strictly according to the approved plan.
  - Performs multiple web searches using Serper.
  - Uses Firecrawl selectively for high-value sources.
  - Focuses on factual, verifiable information.

- **Technical Writer**
  - Synthesizes research findings into a clear, well-structured report.
  - Maintains a neutral, analytical tone.
  - Grounds all conclusions in the conducted research.

---

## Key Characteristics

- **Clarity-first workflow**  
  Research does not start until the user’s intent is explicitly clarified.

- **Plan-driven execution**  
  Research follows a predefined plan rather than ad-hoc searching.

- **Deep web research**  
  Enforces multiple searches to avoid shallow or biased results.

- **Evidence-based reporting**  
  Final output is grounded in sourced findings, not assumptions.

- **Markdown report output**  
  Research results are saved as a professional Markdown report.

---

## Setup

Create a `.env` file with the required API keys:

```env
NVIDIA_API_KEY=your_nvidia_api_key
SERPER_API_KEY=your_serper_api_key
FIRECRAWL_API_KEY=your_firecrawl_api_key
```

## Install Dependencies (using uv)
```
uv sync
```

## Run
```
uv run python src/researchagent/crew.py
```
You will be prompted to enter a topic.
The system will clarify your request, plan the research, execute deep web searches, and generate a final report.

