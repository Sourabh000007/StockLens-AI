from pydantic import BaseModel

from app.models.financial_metric import FinancialMetric


class BalanceSheet(BaseModel):
    total_assets: list[FinancialMetric]
    total_liabilities: list[FinancialMetric]
    total_equity: list[FinancialMetric]
    cash_and_cash_equivalents: list[FinancialMetric]