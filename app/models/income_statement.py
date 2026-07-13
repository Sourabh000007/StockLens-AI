from pydantic import BaseModel


class FinancialMetric(BaseModel):
    year: str
    value: float


class IncomeStatement(BaseModel):
    revenue: list[FinancialMetric]
    gross_profit: list[FinancialMetric]
    operating_income: list[FinancialMetric]
    net_income: list[FinancialMetric]