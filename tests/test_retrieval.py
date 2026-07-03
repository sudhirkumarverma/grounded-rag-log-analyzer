from grounded_rag.retrieval import Retriever

retriever = Retriever()

results = retriever.search(
    "Why did deployment fail?"
)

print("=" * 80)

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")

    print("-" * 80)

    print("Confidence :", result["confidence"])

    print("Distance   :", result["distance"])

    print("Metadata")

    print(result["metadata"])

    print("\nDocument")

    print(result["document"][:500])

print("\nDone.")
