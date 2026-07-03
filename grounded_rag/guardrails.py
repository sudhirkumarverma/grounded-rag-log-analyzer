"""
Retrieval Guardrails
"""

class GuardRails:

    MIN_SIMILARITY = 0.55

    REQUIRED_TYPES = {
        "timeline",
        "incident"
    }

    @staticmethod
    def validate(results):

        if not results:
            return False, "I don't have enough relevant evidence in the indexed enterprise knowledge base to answer this question."

        similarity = results[0]["similarity"]

        if similarity < GuardRails.MIN_SIMILARITY:
            return False, "I don't have enough relevant evidence in the indexed enterprise knowledge base to answer this question."

        source_types = {
            r["metadata"]["source_type"]
            for r in results
        }

        if not (
            source_types &
            GuardRails.REQUIRED_TYPES
        ):
            return False, "I don't have enough relevant evidence in the indexed enterprise knowledge base to answer this question."

        return True, None
