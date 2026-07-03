"""
OpenAI Integration
Grounded RAG Log Analyzer
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

from grounded_rag.config import (
    LLM_MODEL,
    TEMPERATURE,
)
from grounded_rag.prompts import SYSTEM_PROMPT

load_dotenv()


class LLM:
    """
    Wrapper around the OpenAI Chat Completions API.
    """

    def __init__(self):

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY not found. "
                "Please configure it in your .env file."
            )

        self.client = OpenAI(
            api_key=api_key,
        )

    # --------------------------------------------------
    # Build User Prompt
    # --------------------------------------------------

    def _build_prompt(self, context):

        return f"""
QUESTION

{context['question']}

==================================================

DEPLOYMENT TIMELINE

{context['timeline']}

==================================================

HISTORICAL INCIDENTS

{context['incidents']}

==================================================

RUNBOOK

{context['runbooks']}
"""

    # --------------------------------------------------
    # Generate Response
    # --------------------------------------------------

    def generate(self, context):

        prompt = self._build_prompt(context)

        response = self.client.chat.completions.create(
            model=LLM_MODEL,
            temperature=TEMPERATURE,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response.choices[0].message.content.strip()