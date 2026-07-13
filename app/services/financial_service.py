from app.models.income_statement import IncomeStatement
from app.repositories.financial_repository import FinancialRepository


class FinancialService:
    """Business logic for financial statements."""

    def __init__(self, repository: FinancialRepository):
        self.repository = repository

    def get_income_statement(self, symbol: str) -> IncomeStatement:
        """
        Retrieve the company's income statement.
        """
        return self.repository.get_income_statement(symbol)