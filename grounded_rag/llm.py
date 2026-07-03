"""
OpenAI Integration
"""

import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

from grounded_rag.prompts import SYSTEM_PROMPT


class LLM:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate(self, context):

        user_prompt = f"""
QUESTION

{context['question']}

======================================

TIMELINE

{context['timeline']}

======================================

HISTORICAL INCIDENTS

{context['incidents']}

======================================

RUNBOOKS

{context['runbooks']}
"""

        response = self.client.chat.completions.create(
            model="gpt-4.1",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        return response.choices[0].message.content
