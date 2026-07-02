import chromadb
from embeddings import EmbeddingModel
from utils.chunker import chunk_logs

# Initialize embedding model
embedder = EmbeddingModel()

# ChromaDB setup
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="logs")

# Load logs
with open("data/logs.txt", "r") as f:
    logs = f.read()

# Chunk logs properly
chunks = chunk_logs(logs, chunk_size=3)

print(f"Total chunks: {len(chunks)}")

# Embed + store in vector DB
for i, chunk in enumerate(chunks):
    vector = embedder.embed(chunk)

    collection.add(
        ids=[f"log_chunk_{i}"],
        embeddings=vector,
        documents=[chunk],
        metadatas=[{
            "source": "logs.txt",
            "chunk_id": i
        }]
    )

print("✅ Ingestion complete. Vector DB ready.")
