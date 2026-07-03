"""
Context Builder
Grounded RAG Log Analyzer
"""

from typing import List


class ContextBuilder:
    """
    Converts retrieved documents into a structured prompt
    for the LLM.
    """
    def build(self, question: str, results):

        timeline = []
        incidents = []
        runbooks = []

        for item in results:

            source_type = item["metadata"].get("source_type")

            if source_type == "timeline":
                timeline.append(item["document"])

            elif source_type == "incident":
                incidents.append(item["document"])

            elif source_type == "runbook":
                runbooks.append(item["document"])

        return {
            "question": question,
            "timeline": "\n\n".join(timeline),
            "incidents": "\n\n".join(incidents),
            "runbooks": "\n\n".join(runbooks),
        }
