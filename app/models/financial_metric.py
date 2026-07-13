from pydantic import BaseModel


class FinancialMetric(BaseModel):
    year: str
    value: float