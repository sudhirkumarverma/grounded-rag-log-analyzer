from grounded_rag.vector_store import VectorStore

db = VectorStore()

print("=" * 50)

print("Documents :", db.count())

print("=" * 50)
