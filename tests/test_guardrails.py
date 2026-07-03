from grounded_rag.retrieval import Retriever
from grounded_rag.guardrails import GuardRails

retriever = Retriever()

question = input("Question: ")

results = retriever.search(question)

print("\nRetrieved Results")
print("=" * 60)

for i, r in enumerate(results, start=1):

    print(f"\nResult {i}")
    print(f"Source      : {r['metadata']['source_type']}")
    print(f"Similarity  : {r['similarity']:.3f}")
    print(f"Distance    : {r['distance']:.3f}")

    if "incident_id" in r["metadata"]:
        print(f"Incident ID : {r['metadata']['incident_id']}")

print("\n" + "=" * 60)

allowed, message = GuardRails.validate(results)

if allowed:
    print("\n✅ PASS")
else:
    print("\n❌ BLOCKED")
    print(message)
