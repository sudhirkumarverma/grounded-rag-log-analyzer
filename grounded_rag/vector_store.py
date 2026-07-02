"""
Vector Store
Grounded RAG Log Analyzer
"""

from pathlib import Path
import chromadb

from grounded_rag.config import (
    CHROMA_DB_DIR,
    COLLECTION_NAME
)


class VectorStore:

    def __init__(self):

        Path(CHROMA_DB_DIR).mkdir(
            parents=True,
            exist_ok=True
        )

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DB_DIR)
        )

        self.collection = self.client.get_or_create_collection(
            COLLECTION_NAME
        )

    def add_documents(
        self,
        ids,
        documents,
        embeddings,
        metadatas,
    ):

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas,
        )

    def search(
        self,
        embedding,
        top_k,
    ):

        return self.collection.query(
            query_embeddings=embedding.tolist(),
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances",
            ],
        )

    def reset(self):

        try:

            self.client.delete_collection(
                COLLECTION_NAME
            )

        except Exception:
            pass

        self.collection = self.client.get_or_create_collection(
            COLLECTION_NAME
        )

    def count(self):

        return self.collection.count()
