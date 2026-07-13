from pydantic import BaseModel
from app.models.financial_metric import FinancialMetric


class IncomeStatement(BaseModel):
    revenue: list[FinancialMetric]
    gross_profit: list[FinancialMetric]
    operating_income: list[FinancialMetric]
    net_income: list[FinancialMetric]