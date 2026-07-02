# 🧠 Grounded RAG Log Analyzer

> **An AI-powered incident investigation assistant that uses Grounded Retrieval-Augmented Generation (RAG) to analyze enterprise logs, retrieve similar historical incidents, and generate evidence-backed Root Cause Analysis (RCA).**

---

## 📌 Overview

Modern production environments generate massive volumes of logs, making incident investigation slow and error-prone. Traditional keyword search often fails to identify the actual root cause.

Grounded RAG Log Analyzer combines **semantic search**, **vector databases**, and **Large Language Models (LLMs)** to assist engineers in investigating production incidents while ensuring responses remain grounded in retrieved evidence.

Unlike conventional chatbots, the system is designed to **cite supporting evidence**, provide **confidence scores**, and refuse unsupported answers when sufficient evidence is unavailable.

---

## 🚀 Key Features

* 🔍 Semantic search over enterprise logs using embeddings
* 📚 Retrieval-Augmented Generation (RAG)
* 🧠 AI-assisted Root Cause Analysis (RCA)
* 📄 Evidence-backed responses with citations
* 📊 Confidence scoring
* 🛡️ Guardrails to reduce hallucinations
* 📑 Historical incident retrieval
* 📘 Runbook recommendations
* 🖥️ Interactive Streamlit dashboard

---

## 🏗️ Architecture

```text
                   User Question
                          │
                          ▼
                  Streamlit Dashboard
                          │
                          ▼
                  Retrieval Engine
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
     Enterprise Logs   Incident History   Runbooks
          │               │                │
          └───────────────┴────────────────┘
                          │
                          ▼
                  Context Builder
                          │
                          ▼
                     Large Language Model
                          │
                          ▼
     Root Cause + Evidence + Resolution + Confidence
```

---

## 📂 Project Structure

```text
grounded-rag-log-analyzer/

├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── grounded_rag/
│   ├── config.py
│   ├── embeddings.py
│   ├── ingest.py
│   ├── retrieval.py
│   ├── llm.py
│   ├── prompts.py
│   ├── guardrails.py
│   ├── confidence.py
│   └── citation.py
│
├── data/
│   ├── logs/
│   ├── incidents/
│   ├── runbooks/
│   └── sample_questions.json
│
├── scripts/
├── screenshots/
├── tests/
└── chroma_db/
```

---

## ⚙️ Technology Stack

| Component       | Technology                                     |
| --------------- | ---------------------------------------------- |
| Language        | Python 3.11+                                   |
| UI              | Streamlit                                      |
| Vector Database | ChromaDB                                       |
| Embeddings      | Sentence Transformers (BAAI/bge-small-en-v1.5) |
| LLM             | OpenAI GPT-4.1 (configurable)                  |
| Framework       | LangChain                                      |
| Data Processing | Pandas                                         |

---

## 🔄 Workflow

```text
Enterprise Logs
        │
        ▼
Chunking & Metadata Extraction
        │
        ▼
Embedding Generation
        │
        ▼
ChromaDB Vector Store
        │
        ▼
Semantic Retrieval
        │
        ▼
Grounded Prompt Construction
        │
        ▼
Large Language Model
        │
        ▼
Root Cause Analysis
        │
        ▼
Evidence • Confidence • Recommended Resolution
```

---

## 📸 Demo

The application provides:

* AI-generated Root Cause Analysis
* Retrieved evidence
* Historical incident matches
* Recommended remediation
* Confidence score

> Screenshots will be added as the project evolves.

---

## 🛡️ Planned Guardrails

* Input validation
* Prompt injection detection
* Retrieval validation
* Evidence threshold checks
* Hallucination prevention
* Confidence-based refusal

---

## 🚧 Roadmap

### Phase 1

* ✅ Project setup
* ✅ Streamlit UI
* ✅ ChromaDB integration
* ✅ Embedding pipeline
* ✅ Semantic retrieval

### Phase 2

* 🚧 Enterprise synthetic dataset
* 🚧 OpenAI integration
* 🚧 Grounded prompting
* 🚧 Evidence citations

### Phase 3

* ⏳ Guardrails
* ⏳ Confidence scoring
* ⏳ Historical incident retrieval
* ⏳ Runbook recommendations

### Phase 4

* ⏳ Docker support
* ⏳ GitHub Actions
* ⏳ Automated evaluation
* ⏳ Demo video

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/<your-username>/grounded-rag-log-analyzer.git
cd grounded-rag-log-analyzer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate embeddings:

```bash
python -m grounded_rag.ingest
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 Project Goals

This project demonstrates practical applications of:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Explainable AI
* Responsible AI
* Enterprise Log Analytics
* AI-assisted Incident Investigation

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Sudhir Kumar Verma**

Senior Software Engineer | AI & Automation | Embedded Systems | Enterprise Test Automation

---

⭐ If you find this project interesting, consider giving it a star on GitHub.
