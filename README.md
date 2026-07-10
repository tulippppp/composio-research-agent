# AI Research Agent

An automated multi-agent pipeline that researches SaaS APIs, verifies findings, analyzes ecosystem-wide patterns, and generates an interactive HTML report.

Built as part of the **Composio AI Product Operations Internship Take-Home Assignment**.

---
Note: The final submission is available on the submission branch.

## Overview

Researching hundreds of SaaS APIs manually is slow and error-prone.

This project automates the workflow using multiple AI agents that:

- Research an application's API ecosystem
- Verify findings in a second pass
- Store structured JSON outputs
- Analyze cross-application patterns
- Generate a clean HTML dashboard for reviewers

The architecture is designed to scale to hundreds of applications by simply expanding the input CSV.

---

# Architecture

```
Apps CSV
     │
     ▼
Research Agent
     │
     ▼
Verification Agent
     │
     ▼
Structured JSON
     │
     ▼
Analyzer
     │
     ▼
Interactive HTML Report
```

---

# Project Structure

```
.
├── agents/
│   ├── researcher.py
│   ├── verifier.py
│   └── analyzer.py
│
├── data/
│   ├── apps.csv
│   ├── raw/
│   └── verified/
│
├── models/
│   └── app.py
│
├── prompts/
│   └── research.txt
│
├── templates/
│   └── report.html
│
├── utils/
│   ├── gemini.py
│   └── io.py
│
├── main.py
├── analyze.py
├── generate_report.py
└── report.html
```

---

# Features

- AI-powered API research

- Second-pass verification

- Structured Pydantic models

- JSON output

- Ecosystem-wide analysis

- Interactive HTML dashboard

---

# Information Collected

For each application the agent captures:

- Category
- Description
- Authentication methods
- Self-serve vs gated access
- API surface
- MCP availability
- Buildability verdict
- Confidence score
- Evidence URLs

---

# Multi-Agent Workflow

### Research Agent

Uses Gemini to research an application's developer ecosystem and generate structured JSON.

---

### Verification Agent

Performs a second validation pass to:

- verify claims
- reduce hallucinations
- correct unsupported information
- adjust confidence scores

---

### Analyzer

Aggregates verified results to identify patterns such as:

- authentication trends
- self-serve adoption
- MCP availability
- common blockers
- buildability statistics

---

### Report Generator

Generates an interactive HTML dashboard using Jinja2.

---

# Installation

Clone the repository

```bash
git clone https://github.com/tulippppp/composio-research-agent.git
cd composio-research-agent
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate it

macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=your_api_key_here
```

---

# Usage

Run the research pipeline

```bash
python main.py
```

Analyze results

```bash
python analyze.py
```

Generate report

```bash
python generate_report.py
```

---

# Sample Results

Current sample includes research for:

- Slack
- GitHub
- Notion
- Linear
- Discord
- Stripe

Example insights:

- OAuth 2.0 is the dominant authentication method.
- Most developer platforms are self-service.
- MCP support is becoming increasingly common.
- Public APIs enable rapid toolkit development.

---

# Tech Stack

- Python 3.11
- Google Gemini API
- Pydantic
- Jinja2
- HTML/CSS
- JSON

---

# Notes

This submission demonstrates the complete research and verification pipeline on a representative subset of applications.

The system is designed to scale to the full 100-application dataset by expanding the input CSV.

---

# Deliverables

- Automated multi-agent research pipeline
- Structured JSON outputs
- Ecosystem analysis
- Interactive HTML dashboard
- Source code

---

Built with ❤️ for the **Composio AI Product Operations Internship Assignment**.
