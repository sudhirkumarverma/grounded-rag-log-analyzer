from grounded_rag.embeddings import EmbeddingEngine

engine = EmbeddingEngine()

vector = engine.embed("Deployment failed because PostgreSQL timed out")

print("=" * 50)

print(type(vector))
print(vector.shape)

print(vector[0][:10])

print("=" * 50)

print("Embedding engine working successfully.")
