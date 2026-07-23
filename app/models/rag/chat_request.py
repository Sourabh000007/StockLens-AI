from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Request model for annual report chat.
    """

    company: str

    report_year: int

    question: str