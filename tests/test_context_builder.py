from grounded_rag.retrieval import Retriever
from grounded_rag.context_builder import ContextBuilder

retriever = Retriever()

results = retriever.search(
    "Why did deployment fail?"
)

builder = ContextBuilder()

prompt = builder.build(
    "Why did deployment fail?",
    results
)

print(prompt)
