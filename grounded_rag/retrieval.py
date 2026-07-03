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
