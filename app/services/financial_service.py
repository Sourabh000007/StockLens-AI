from app.models.income_statement import IncomeStatement
from app.repositories.financial_repository import FinancialRepository
from app.models.balance_sheet import BalanceSheet


class FinancialService:
    """Business logic for financial statements."""

    def __init__(self, repository: FinancialRepository):
        self.repository = repository

    def get_income_statement(self, symbol: str) -> IncomeStatement:
        """
        Retrieve the company's income statement.
        """
        return self.repository.get_income_statement(symbol)
    
    def get_balance_sheet(self, symbol: str) -> BalanceSheet:
        """
        Retrieve the company's balance sheet.
        """
        return self.repository.get_balance_sheet(symbol)