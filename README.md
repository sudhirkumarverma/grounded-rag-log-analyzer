# grounded-rag-log-analyzer
AI-powered Grounded RAG system for log analysis and root cause detection with evidence-backed explanations, confidence scoring, and refusal behavior.


# 🧠 Grounded RAG Log Analyzer

An AI-powered **Root Cause Analysis system** using **Grounded Retrieval-Augmented Generation (RAG)** over enterprise logs with evidence-backed reasoning, confidence scoring, and refusal behavior.

---

## 🚀 Key Features

- 📊 Semantic log search using embeddings (ChromaDB)
- 🧠 Retrieval-Augmented Generation (RAG)
- 📌 Evidence-grounded root cause analysis
- 📉 Confidence scoring for every prediction
- 🚫 Refusal mechanism when evidence is weak
- 🖥️ Interactive Streamlit UI
- 🔍 Explainable AI (shows exact log evidence)

---

## 🏗️ Architecture


Logs → Chunking → Embeddings → Vector DB (ChromaDB)
↓
Retrieval
↓
LLM Reasoning
↓
Root Cause + Evidence + Confidence


---

## 📦 Tech Stack

- Python 3.12
- Streamlit
- ChromaDB
- SentenceTransformers (bge-small-en)
- LangChain
- OpenAI / LLM-ready design

---

## 📊 Example Use Case

**Question:**
> Why did deployment fail?

**Output:**
- Root Cause: Database migration timeout
- Evidence: log chunks from Jenkins + PostgreSQL errors
- Confidence: 87%

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python ingest.py
streamlit run app.py
📁 Project Structure
grounded-rag-log-analyzer/
│── app.py
│── ingest.py
│── rag.py
│── embeddings.py
│── confidence.py
│── prompts.py
│
├── data/
├── utils/
├── chroma_db/
🎯 Why this project matters

Modern AI systems fail due to hallucinations.
This project demonstrates:

Grounded reasoning (no hallucination)
Explainability (evidence traceability)
Confidence-aware AI decisions
Enterprise-style log analysis pipeline
🔥 Future Enhancements
Hybrid search (BM25 + Vector)
LLM integration (GPT / Claude)
Kubernetes log ingestion
Real-time monitoring dashboard
Incident timeline visualization
👨   Author

Sudhir Verma
AI / Automation / Systems Engineer
