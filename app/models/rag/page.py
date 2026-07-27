from pydantic import BaseModel


class ReportPage(BaseModel):
    """
    Represents one page of an annual report.
    """

    page_number: int

    text: str