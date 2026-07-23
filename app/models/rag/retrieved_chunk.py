from pydantic import BaseModel


class RetrievedChunk(BaseModel):
    """
    Represents one retrieved chunk.
    """

    chunk_id: str

    text: str

    company: str

    report_year: int