from pydantic import BaseModel

from app.models.rag.retrieved_chunk import RetrievedChunk


class ChatResponse(BaseModel):
    """
    Response returned by the annual report chat API.
    """

    answer: str

    sources: list[RetrievedChunk]