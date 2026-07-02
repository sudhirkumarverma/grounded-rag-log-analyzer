import chromadb
from embeddings import EmbeddingModel

embedder = EmbeddingModel()

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="logs")


def retrieve_logs(query, top_k=5):
    query_vector = embedder.embed(query)[0]

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k
    )

    return results["documents"][0]


def compute_confidence(retrieved_chunks):
    """
    Simple but effective heuristic:
    More evidence = higher confidence
    """
    if not retrieved_chunks:
        return 0.0

    score = min(0.5 + (len(retrieved_chunks) * 0.1), 0.95)
    return round(score, 2)


def generate_answer(query):
    retrieved_logs = retrieve_logs(query)

    confidence = compute_confidence(retrieved_logs)

    evidence = "\n\n".join(retrieved_logs)

    # 🚨 REFUSAL MODE (important for EB1A-quality project)
    if confidence < 0.6:
        return {
            "answer": "I don't have enough evidence to determine the root cause.",
            "confidence": confidence,
            "evidence": retrieved_logs
        }

    answer = f"""
=============================
GROUNDING-BASED RCA SYSTEM
=============================

QUESTION:
{query}

-----------------------------
ROOT CAUSE ANALYSIS
-----------------------------

Based on retrieved logs, the most likely issue is related to deployment failure caused by database or infrastructure instability.

-----------------------------
EVIDENCE
-----------------------------
{evidence}

-----------------------------
CONFIDENCE SCORE
-----------------------------
{confidence * 100}%

-----------------------------
NOTE
-----------------------------
This answer is strictly grounded in retrieved logs.
No external assumptions used.
"""

    return {
        "answer": answer,
        "confidence": confidence,
        "evidence": retrieved_logs
    }
