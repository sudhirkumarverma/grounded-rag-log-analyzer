from grounded_rag.retrieval import Retriever
from grounded_rag.context_builder import ContextBuilder
from grounded_rag.llm import LLM

retriever = Retriever()

results = retriever.search(
    "Why did deployment fail?"
)

builder = ContextBuilder()

context = builder.build(
    "Why did deployment fail?",
    results,
)

llm = LLM()

answer = llm.generate(context)

print(answer)
