"""
Grounded RAG Pipeline

Orchestrates the complete AI workflow.
"""

from grounded_rag.retrieval import Retriever
from grounded_rag.guardrails import GuardRails
from grounded_rag.context_builder import ContextBuilder
from grounded_rag.llm import LLM


class GroundedRAGPipeline:

    def __init__(self):

        self.retriever = Retriever()
        self.context_builder = ContextBuilder()
        self.llm = LLM()

    def ask(self, question: str):

        # Step 1 - Retrieve evidence
        results = self.retriever.search(question)

        # Step 2 - Validate evidence
        allowed, message = GuardRails.validate(results)

        if not allowed:

            return {
                "allowed": False,
                "message": message,
                "answer": None,
                "results": results,
            }

        # Step 3 - Build context
        context = self.context_builder.build(
            question,
            results,
        )

        # Step 4 - Generate answer
        answer = self.llm.generate(context)

        return {
            "allowed": True,
            "message": None,
            "answer": answer,
            "results": results,
        }
