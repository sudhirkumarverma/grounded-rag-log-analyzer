# 🔍 Grounded RAG Incident Investigator

> **An Enterprise AI application that performs evidence-grounded Root Cause Analysis (RCA) using Retrieval-Augmented Generation (RAG).**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)]()
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1-green.svg)]()
[![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple.svg)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()

---

## Overview

Grounded RAG Incident Investigator is an enterprise AI application that analyzes deployment failures using **Retrieval-Augmented Generation (RAG)**.

Unlike a traditional chatbot, this application **does not answer from the model's memory**. Every response is generated only after retrieving supporting evidence from an indexed enterprise knowledge base.

The knowledge base consists of:

- Deployment timelines
- Historical production incidents
- Operational runbooks

This grounding approach significantly reduces hallucinations and improves the reliability of AI-generated Root Cause Analysis (RCA).

---

## Key Features

- Evidence-grounded AI responses
- Enterprise incident investigation
- Retrieval-Augmented Generation (RAG)
- ChromaDB vector search
- Sentence Transformer embeddings
- OpenAI GPT-4.1 integration
- Multi-layer guardrails
- Operational runbook retrieval
- Historical incident correlation
- Professional Streamlit dashboard

---

# System Architecture

```

                User Question
                      │
                      ▼
             Question Validation
                      │
                      ▼
               Semantic Retrieval
                      │
                      ▼
              ChromaDB Vector Store
                      │
                      ▼
             Retrieved Enterprise Evidence
          (Timelines + Incidents + Runbooks)
                      │
                      ▼
               Context Builder
                      │
                      ▼
               OpenAI GPT-4.1
                      │
                      ▼
             Grounded AI Response

```

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11 |
| UI | Streamlit |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Vector Database | ChromaDB |
| LLM | OpenAI GPT-4.1 |
| Dataset | Enterprise Incident Logs |
| Retrieval | Semantic Search |
| Prompting | Evidence Grounded |
| Architecture | Retrieval-Augmented Generation |

---

# Project Structure

```text
grounded-rag-log-analyzer/
│
├── app.py
│
├── grounded_rag/
│   ├── config.py
│   ├── embeddings.py
│   ├── ingest.py
│   ├── vector_store.py
│   ├── retrieval.py
│   ├── guardrails.py
│   ├── context_builder.py
│   ├── prompts.py
│   ├── llm.py
│   └── pipeline.py
│
├── data/
│   ├── logs/
│   ├── incidents/
│   └── runbooks/
│
├── tests/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

---

# How It Works

The application follows a Retrieval-Augmented Generation (RAG) pipeline.

1. The user submits an enterprise incident question.
2. Guardrails validate that the question is meaningful and relevant.
3. The embedding model converts the question into a vector representation.
4. ChromaDB retrieves the most relevant enterprise documents.
5. Retrieved evidence is organized into deployment timelines, historical incidents, and runbooks.
6. The LLM receives only the retrieved evidence as context.
7. A grounded Root Cause Analysis is generated.
8. Evidence and similarity scores are displayed in the user interface.

---

# Why Grounded RAG?

Traditional LLMs can generate confident but unsupported answers.

This project mitigates that risk by ensuring that responses are based only on retrieved enterprise evidence.

Benefits include:

- Reduced hallucinations
- Traceable evidence
- Explainable AI
- Improved operational reliability
- Enterprise-ready workflow
---

# Installation

## Clone the repository

```bash
git clone https://github.com/sudhirkumarverma/grounded-rag-log-analyzer.git

cd grounded-rag-log-analyzer
```

---

## Create a virtual environment

### macOS / Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# Configuration

Create a `.env` file in the project root.

```text
OPENAI_API_KEY=your_openai_api_key
```

---

# Build the Knowledge Base

Before launching the application, ingest the enterprise knowledge base.

```bash
python -m grounded_rag.ingest
```

Example output:

```text
Loading enterprise logs...

Loaded 50 deployment timelines

Loaded 50 historical incidents

Loaded 1 deployment runbook

Generating embeddings...

Successfully indexed 101 documents.

Knowledge Base Ready.
```

---

# Run the Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

# Example Questions

### Deployment Analysis

```
Why did deployment fail?
```

### Kubernetes

```
What caused Kubernetes deployment failure?
```

### Authentication

```
Why are image pulls failing?
```

### Operational Guidance

```
Show deployment runbook.
```

### Root Cause Analysis

```
Explain the deployment failure.
```

---

# Example Response

```text
ROOT CAUSE

Container registry authentication failed,
causing Kubernetes image pull failures.

EVIDENCE

Deployment timelines indicate repeated image
pull failures.

Historical incidents INC-1047, INC-1050 and
INC-1024 report identical failure patterns.

The deployment runbook recommends refreshing
registry credentials.

RECOMMENDED RESOLUTION

Refresh registry credentials.

Retry deployment.

Rotate credentials before expiration.

INCIDENTS REFERENCED

INC-1047

INC-1050

INC-1024
```

---

# Guardrails

The application prevents unsupported or low-confidence responses using multiple validation layers.

Current guardrails include:

- Question validation
- Domain relevance detection
- Retrieval validation
- Minimum evidence threshold
- Minimum similarity threshold
- Grounded prompting
- Evidence-only response generation

If sufficient supporting evidence is unavailable, the application declines to answer instead of generating unsupported information.

---

# User Interface

The Streamlit dashboard provides:

- Enterprise question interface
- AI-generated Root Cause Analysis
- Evidence strength indicators
- Similarity metrics
- Retrieved enterprise evidence
- Knowledge base summary
- Technology overview

---

# Screenshots

The following screenshots demonstrate the application workflow.

```
screenshots/

home.png

analysis.png

retrieved_evidence.png

guardrail_validation.png
```

> Add screenshots after running the application.

---

# Current Limitations

Version 1.0 intentionally focuses on semantic retrieval.

Current limitations include:

- Semantic retrieval only
- No exact metadata lookup
- Single enterprise runbook
- Demonstration dataset

These choices keep the architecture simple while illustrating an enterprise-grade Retrieval-Augmented Generation workflow.

---

# Roadmap

## Version 1.1

Planned improvements:

- Hybrid retrieval
- Exact incident lookup
- Metadata filtering
- Multi-runbook support
- Incident timeline visualization
- Confidence calibration
- Exportable investigation reports

## Version 1.2

Future enhancements:

- Multi-agent incident investigation
- Live enterprise log ingestion
- Slack and Microsoft Teams integration
- Kubernetes API integration
- Grafana integration
- Real-time monitoring
- Automated remediation suggestions

---# Testing

The project includes unit tests for the major pipeline components.

Run all tests:

```bash
python -m pytest
```

Run individual tests:

```bash
python -m tests.test_embeddings

python -m tests.test_retrieval

python -m tests.test_guardrails

python -m tests.test_pipeline

python -m tests.test_llm
```

---

# Design Principles

This project was designed around the following engineering principles:

- Modular architecture
- Separation of concerns
- Evidence-grounded AI
- Retrieval before generation
- Explainable responses
- Guardrail-driven validation
- Production-inspired code organization

The application intentionally separates ingestion, retrieval, validation, prompt construction, language model interaction, and presentation into independent modules, making the system easier to understand, test, and extend.

---

# Project Highlights

This project demonstrates practical implementation of modern Generative AI concepts, including:

- Retrieval-Augmented Generation (RAG)
- Vector embeddings
- Semantic search
- Enterprise knowledge retrieval
- Grounded prompting
- AI guardrails
- Context construction
- ChromaDB vector database integration
- OpenAI API integration
- Streamlit application development

---

# Lessons Learned

Building this project reinforced several important engineering concepts:

- High-quality retrieval is just as important as the language model itself.
- Grounding responses with enterprise evidence significantly reduces hallucinations.
- Guardrails improve reliability by preventing unsupported answers.
- Modular architecture simplifies testing, maintenance, and future enhancements.
- A clean user experience is essential for making AI systems usable in enterprise environments.

---

# Future Enhancements

Potential future enhancements include:

- Hybrid semantic and metadata retrieval
- Exact incident ID lookup
- Multi-runbook support
- Enterprise authentication (SSO/OAuth)
- User feedback collection
- Investigation report export (PDF/Markdown)
- Real-time log ingestion
- Integration with monitoring platforms such as Grafana, Prometheus, or Splunk
- REST API for external integrations
- CI/CD deployment with Docker and Kubernetes

---

# License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

# Author

**Sudhir Kumar Verma**

Senior Software Engineer | Test Automation | Embedded Systems | Generative AI

GitHub: [github.com/sudhirkumarverma](https://github.com/sudhirkumarverma)

LinkedIn: [linkedin.com/in/sudhir-kumar-verma-b866258](https://www.linkedin.com/in/sudhir-kumar-verma-b866258)

---

# Acknowledgements

This project uses the following open-source technologies:

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- OpenAI API
- pandas
- python-dotenv

Special thanks to the open-source community for providing the tools and libraries that made this project possible.

---

# Support

If you find this project useful:

⭐ Star the repository

🐞 Report issues

💡 Submit feature requests

🤝 Contributions are welcome through pull requests.

---

# Final Notes

Grounded RAG Incident Investigator demonstrates how Retrieval-Augmented Generation can be applied to enterprise incident investigation while keeping AI responses grounded in verifiable evidence.

Rather than relying solely on a language model's internal knowledge, the application retrieves deployment timelines, historical incidents, and operational runbooks before generating responses. This evidence-first approach improves transparency, reduces hallucinations, and provides a foundation for trustworthy AI-assisted Root Cause Analysis.

Although version **1.0** focuses on semantic retrieval, the architecture has been intentionally designed to support future enhancements such as hybrid retrieval, metadata-aware search, and real-time enterprise integrations.

This project serves as a practical reference implementation for developers exploring enterprise AI systems built on Retrieval-Augmented Generation.

---

## Repository Status

**Version:** 1.0

**Status:** Version 1.0

**Architecture:** Stable

**License:** MIT

**Last Updated:** July 2026