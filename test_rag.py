from rag import generate_answer

query = "Why did it rain today?"

result = generate_answer(query)

print(result["answer"])
print("\nConfidence:", result["confidence"])
