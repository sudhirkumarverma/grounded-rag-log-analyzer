"""
Embedding Engine
Grounded RAG Log Analyzer
"""

from sentence_transformers import SentenceTransformer
from grounded_rag.config import EMBEDDING_MODEL


class EmbeddingEngine:
    """
    Singleton embedding engine.
    Loads the embedding model only once.
    """

    _model = None

    def __init__(self):

        if EmbeddingEngine._model is None:
            print(f"Loading embedding model: {EMBEDDING_MODEL}")
            EmbeddingEngine._model = SentenceTransformer(
                EMBEDDING_MODEL
            )

    def embed(self, text):

        if isinstance(text, str):
            text = [text]

        embeddings = EmbeddingEngine._model.encode(
            text,
            normalize_embeddings=True,
            show_progress_bar=False
        )

        return embeddings
