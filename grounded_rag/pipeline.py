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

        # --------------------------------------------------
        # Step 1 - Validate the user's question
        # --------------------------------------------------

        allowed, message = GuardRails.validate_question(question)

        if not allowed:
            return {
                "allowed": False,
                "message": message,
                "answer": None,
                "results": [],
            }

        # --------------------------------------------------
        # Step 2 - Retrieve relevant evidence
        # --------------------------------------------------

        results = self.retriever.search(question)

        # --------------------------------------------------
        # Step 3 - Validate retrieved evidence
        # --------------------------------------------------

        allowed, message = GuardRails.validate_retrieval(results)

        if not allowed:
            return {
                "allowed": False,
                "message": message,
                "answer": None,
                "results": results,
            }

        # --------------------------------------------------
        # Step 4 - Build grounded context
        # --------------------------------------------------

        context = self.context_builder.build(
            question,
            results,
        )

        # --------------------------------------------------
        # Step 5 - Generate grounded response
        # --------------------------------------------------

        answer = self.llm.generate(context)

        # --------------------------------------------------
        # Step 6 - Return final response
        # --------------------------------------------------

        return {
            "allowed": True,
            "message": None,
            "answer": answer,
            "results": results,
        }
