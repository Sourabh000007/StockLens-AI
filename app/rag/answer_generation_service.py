from app.ai.groq_client import GroqClient
from app.ai.rag.answer_prompt_builder import AnswerPromptBuilder
from app.rag.retrieval_service import RetrievalService


class AnswerGenerationService:
    """
    Generate answers using the annual report.
    """

    def __init__(self):

        self.retrieval_service = RetrievalService()

        self.prompt_builder = AnswerPromptBuilder()

        self.groq_client = GroqClient()

    def ask(
        self,
        question: str,
        company: str,
        report_year: int,
    ) -> str:
        """
        Answer a question using RAG.
        """

        context = self.retrieval_service.retrieve(
            question=question,
            company=company,
            report_year=report_year,
        )

        prompt = self.prompt_builder.build(
            question=question,
            context=context,
        )

        return self.groq_client.generate(prompt)