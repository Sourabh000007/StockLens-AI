from pydantic import BaseModel

from app.models.rag.retrieved_chunk import RetrievedChunk


class AnnualReportAnswer(BaseModel):
    """
    Complete response from the annual report chat.
    """

    answer: str

    sources: list[RetrievedChunk]