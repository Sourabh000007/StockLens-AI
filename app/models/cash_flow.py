from pydantic import BaseModel

from app.models.financial_metric import FinancialMetric


class CashFlow(BaseModel):
    operating_cash_flow: list[FinancialMetric]
    investing_cash_flow: list[FinancialMetric]
    financing_cash_flow: list[FinancialMetric]