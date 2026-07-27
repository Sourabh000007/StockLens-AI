from app.ai.prompts.base_prompt import BasePrompt
from app.models.rag import RetrievedChunk


class AnnualReportPrompt(BasePrompt):
    """
    Builds prompts for annual report Q&A.
    """

    @staticmethod
    def build(
        question: str,
        context: list[RetrievedChunk],
    ) -> str:

        report_context = "\n\n".join(
            chunk.text
            for chunk in context
        )

        return f"""
{BasePrompt.SYSTEM_INSTRUCTIONS}

Annual Report Context
---------------------

{report_context}

Question
--------

{question}

Answer:
"""