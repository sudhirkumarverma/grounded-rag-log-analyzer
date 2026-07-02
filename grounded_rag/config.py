"""
Grounded RAG Log Analyzer

Central Configuration
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

LOG_DIR = DATA_DIR / "logs"

INCIDENT_DIR = DATA_DIR / "incidents"

RUNBOOK_DIR = DATA_DIR / "runbooks"

CHROMA_DB_DIR = PROJECT_ROOT / "chroma_db"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

COLLECTION_NAME = "enterprise_logs"

TOP_K = 5

LLM_MODEL = "gpt-4.1"

TEMPERATURE = 0
