from app.ai.groq_client import GroqClient
from app.ai.rag.answer_prompt_builder import AnswerPromptBuilder
from app.models.rag import AnnualReportAnswer
from app.rag.retrieval_service import RetrievalService


class AnnualReportChatService:
    """
    Coordinates the complete RAG pipeline.
    """

    def __init__(self):

        self.retrieval_service = RetrievalService()

        self.prompt_builder = AnswerPromptBuilder()

        self.groq_client = GroqClient()

    def ask(
        self,
        company: str,
        report_year: int,
        question: str,
    ) -> AnnualReportAnswer:
        """
        Answer a question using the indexed annual report.
        """

        chunks = self.retrieval_service.retrieve(
            question=question,
            company=company,
            report_year=report_year,
        )

        prompt = self.prompt_builder.build(
            question=question,
            context=chunks,
        )

        answer = self.groq_client.generate(prompt)

        return AnnualReportAnswer(
            answer=answer,
            sources=chunks,
        )