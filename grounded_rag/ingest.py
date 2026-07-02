"""
Grounded RAG Log Analyzer

Enterprise Knowledge Base Ingestion
"""

from __future__ import annotations

import pandas as pd
from pathlib import Path
from collections import defaultdict

from grounded_rag.config import (
    LOG_DIR,
    INCIDENT_DIR,
    RUNBOOK_DIR
)

from grounded_rag.embeddings import EmbeddingEngine
from grounded_rag.vector_store import VectorStore


class KnowledgeIngestor:

    def __init__(self):

        self.embedder = EmbeddingEngine()

        self.vector_store = VectorStore()

        self.documents = []

        self.metadatas = []

        self.ids = []

    # --------------------------------------------------
    # Enterprise Logs
    # --------------------------------------------------

    def load_enterprise_logs(self):

        csv_file = LOG_DIR / "enterprise_logs.csv"

        print(f"Loading {csv_file}")

        df = pd.read_csv(csv_file)

        grouped = defaultdict(list)

        metadata = {}

        for _, row in df.iterrows():

            incident_id = row["incident_id"]

            grouped[incident_id].append(row)

            metadata[incident_id] = {
                "source_type": "timeline",
                "incident_id": incident_id,
                "service": row["service"],
                "environment": row["environment"],
            }

        for incident_id, rows in grouped.items():

            rows = sorted(
                rows,
                key=lambda r: r["timestamp"]
            )

            timeline = []

            for row in rows:

                timeline.append(
                    f"[{row['timestamp']}] "
                    f"{row['source']} "
                    f"{row['severity']} "
                    f"{row['message']}"
                )

            document = (
                f"Incident Timeline\n\n"
                f"Incident ID: {incident_id}\n\n"
                + "\n".join(timeline)
            )

            self.documents.append(document)

            self.metadatas.append(metadata[incident_id])

            self.ids.append(
                f"timeline_{incident_id}"
            )

        print(
            f"Loaded {len(grouped)} incident timelines"
        )

    # --------------------------------------------------
    # Historical Incidents
    # --------------------------------------------------

    def load_incidents(self):

        csv_file = (
            INCIDENT_DIR /
            "incident_history.csv"
        )

        print(f"Loading {csv_file}")

        df = pd.read_csv(csv_file)

        for _, row in df.iterrows():

            document = f"""
Historical Incident

Incident ID : {row['incident_id']}

Title

{row['title']}

Root Cause

{row['root_cause']}

Resolution

{row['resolution']}

Lessons Learned

{row['lessons_learned']}
"""

            self.documents.append(document)

            self.metadatas.append({

                "source_type": "incident",

                "incident_id": row["incident_id"]

            })

            self.ids.append(

                f"incident_{row['incident_id']}"

            )

        print(

            f"Loaded {len(df)} historical incidents"

        )

    # --------------------------------------------------
    # Runbook
    # --------------------------------------------------

    def load_runbook(self):

        runbook = (
            RUNBOOK_DIR /
            "deployment_runbook.md"
        )

        print(f"Loading {runbook}")

        text = runbook.read_text(
            encoding="utf-8"
        )

        self.documents.append(text)

        self.metadatas.append({

            "source_type": "runbook",

            "title": "Deployment Failure Runbook"

        })

        self.ids.append("runbook_deployment")

    # --------------------------------------------------
    # Build Vector Store
    # --------------------------------------------------

    def build_vector_store(self):

        print("\nGenerating embeddings...")

        embeddings = self.embedder.embed(self.documents)

        print(f"Generated {len(embeddings)} embeddings")

        print("\nResetting vector store...")

        self.vector_store.reset()

        print("Adding documents to ChromaDB...")

        self.vector_store.add_documents(
            ids=self.ids,
            documents=self.documents,
            embeddings=embeddings,
            metadatas=self.metadatas,
        )

        print(
            f"Successfully indexed {self.vector_store.count()} documents."
        )

    # --------------------------------------------------
    # Execute Complete Pipeline
    # --------------------------------------------------

    def ingest(self):

        self.load_enterprise_logs()

        self.load_incidents()

        self.load_runbook()

        print("\n----------------------------------------")
        print(f"Total Documents : {len(self.documents)}")
        print("----------------------------------------")

        self.build_vector_store()

        print("\nIngestion completed successfully.")


# --------------------------------------------------
# Main
# --------------------------------------------------

def main():

    print("=" * 60)
    print("Grounded RAG Log Analyzer")
    print("Knowledge Base Ingestion")
    print("=" * 60)

    ingestor = KnowledgeIngestor()

    ingestor.ingest()

    print("\nKnowledge Base Ready.")

    print("\nIndexed Sources")

    timeline_count = sum(
        1 for m in ingestor.metadatas
        if m["source_type"] == "timeline"
    )

    incident_count = sum(
        1 for m in ingestor.metadatas
        if m["source_type"] == "incident"
    )

    runbook_count = sum(
        1 for m in ingestor.metadatas
        if m["source_type"] == "runbook"
    )

    print(f"  Timelines : {timeline_count}")
    print(f"  Incidents : {incident_count}")
    print(f"  Runbooks  : {runbook_count}")


if __name__ == "__main__":
    main()
