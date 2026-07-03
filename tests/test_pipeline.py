from grounded_rag.pipeline import GroundedRAGPipeline

pipeline = GroundedRAGPipeline()

while True:

    print()

    question = input("Question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    response = pipeline.ask(question)

    print("\n" + "=" * 80)

    if not response["allowed"]:

        print(response["message"])

        continue

    print(response["answer"])

    print("\nRetrieved Evidence")

    print("-" * 80)

    for item in response["results"]:

        metadata = item["metadata"]

        print(
            f"{metadata['source_type']:10}"
            f" | Similarity: {item['similarity']:.3f}"
        )

        if "incident_id" in metadata:

            print(
                f"Incident : {metadata['incident_id']}"
            )

        print()

    print("=" * 80)
