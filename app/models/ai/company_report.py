from pydantic import BaseModel


class AICompanyReport(BaseModel):
    """
    Structured AI analysis for a company.
    """

    summary: str

    financial_health: str

    news_summary: str

    strengths: list[str]

    risks: list[str]

    investment_thesis: str