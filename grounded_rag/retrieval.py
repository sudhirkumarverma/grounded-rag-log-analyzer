"""
Grounded RAG Log Analyzer

Retrieval Engine
"""

from grounded_rag.embeddings import EmbeddingEngine
from grounded_rag.vector_store import VectorStore
from grounded_rag.config import TOP_K


class Retriever:

    def __init__(self):

        self.embedder = EmbeddingEngine()

        self.vector_store = VectorStore()

    # --------------------------------------------------
    # Search
    # --------------------------------------------------
    def search(self, question):

        embedding = self.embedder.embed(question)

        results = self.vector_store.search(
            embedding=embedding,
            top_k=10,   # retrieve more initially
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        grouped = {
            "timeline": None,
            "incident": None,
            "runbook": None,
        }

        extras = []

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances,
        ):

            item = {
                "document": document,
                "metadata": metadata,
                "distance": float(distance),
                "confidence": round(max(0.0, 1.0 - float(distance)), 3),
            }

            source = metadata.get("source_type")

            if source in grouped and grouped[source] is None:
                grouped[source] = item
            else:
                extras.append(item)

        final_results = []

        for key in ["timeline", "incident", "runbook"]:
            if grouped[key]:
                final_results.append(grouped[key])

        final_results.extend(extras)

        return final_results[:TOP_K]
    def search1(self, question):

        embedding = self.embedder.embed(question)

        results = self.vector_store.search(
            embedding=embedding,
            top_k=TOP_K,
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        response = []

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances,
        ):

            response.append(
                {
                    "document": document,
                    "metadata": metadata,
                    "distance": float(distance),
                    "confidence": round(
                        max(0.0, 1.0 - float(distance)),
                        3,
                    ),
                }
            )

        response.sort(
            key=lambda x: x["distance"]
        )

        return response
