"""
Guardrails
Grounded RAG Incident Investigator

Provides multiple validation layers before invoking the LLM.
"""

import re


class GuardRails:

    # Minimum similarity for the best retrieved document
    MIN_SIMILARITY = 0.55

    # Minimum number of retrieved documents
    MIN_DOCUMENTS = 2

    # Domain keywords
    DOMAIN_KEYWORDS = {
        "deployment",
        "deploy",
        "incident",
        "failure",
        "failed",
        "error",
        "issue",
        "service",
        "application",
        "server",
        "kubernetes",
        "pod",
        "container",
        "docker",
        "database",
        "postgres",
        "redis",
        "timeout",
        "latency",
        "rollback",
        "runbook",
        "root cause",
        "rca",
        "log",
        "logs",
        "health",
        "restart",
        "api",
        "microservice",
        "authentication",
        "authorization",
    }

    @staticmethod
    def validate_question(question: str):

        question = question.strip().lower()

        if len(question) < 8:
            return False, "Please enter a meaningful question."

        words = re.findall(r"[a-zA-Z]+", question)

        if len(words) < 3:
            return False, "Please enter a more descriptive question."

        keyword_found = any(
            keyword in question
            for keyword in GuardRails.DOMAIN_KEYWORDS
        )

        incident_pattern = re.search(
            r"inc-\d+",
            question,
            re.IGNORECASE,
        )

        if not keyword_found and not incident_pattern:
            return (
                False,
                "Your question doesn't appear to be related to enterprise incidents or deployments."
            )

        return True, None

    @staticmethod
    def validate_retrieval(results):

        if not results:
            return (
                False,
                "I couldn't find relevant evidence in the indexed knowledge base."
            )

        if len(results) < GuardRails.MIN_DOCUMENTS:
            return (
                False,
                "Insufficient supporting evidence was retrieved."
            )

        if results[0]["similarity"] < GuardRails.MIN_SIMILARITY:
            return (
                False,
                "The retrieved evidence is not sufficiently relevant to answer this question."
            )

        source_types = {
            r["metadata"]["source_type"]
            for r in results
        }

        if "timeline" not in source_types:
            return (
                False,
                "No deployment timeline was found for this request."
            )

        if "incident" not in source_types:
            return (
                False,
                "No historical incident was found for this request."
            )

        return True, None