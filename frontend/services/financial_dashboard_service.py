from app.models.income_statement import IncomeStatement
from app.repositories.financial_repository import FinancialRepository
from app.services.financial_service import FinancialService


class FinancialDashboardService:

    def __init__(self):
        repository = FinancialRepository()
        self.financial_service = FinancialService(repository)

    def get_income_statement(
        self,
        symbol: str,
    ) -> IncomeStatement:
        """
        Retrieve the company's income statement.
        """

        return self.financial_service.get_income_statement(symbol)