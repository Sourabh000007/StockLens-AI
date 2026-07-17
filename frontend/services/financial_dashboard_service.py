from app.models.income_statement import IncomeStatement
from app.repositories.financial_repository import FinancialRepository
from app.services.financial_service import FinancialService
from app.models.balance_sheet import BalanceSheet


class FinancialDashboardService:

    def __init__(self):
        repository = FinancialRepository()
        self.financial_service = FinancialService(repository)

    def get_income_statement(self,symbol: str) -> IncomeStatement:
        
        """
        Retrieve the company's income statement.
        """

        return self.financial_service.get_income_statement(symbol)
    
    def get_cash_flow(self,symbol: str,):
        """
        Retrieve the cash flow statement.
        """

        return self.financial_service.get_cash_flow(
            symbol,
        )
        
    def get_balance_sheet(self,symbol: str) -> BalanceSheet:

        """
        Retrieve the company's balance sheet.
        """

        return self.financial_service.get_balance_sheet(symbol)
    
    def get_cash_flow(self,symbol: str) :
        """
        Retrieve the company's cash flow statement.
        """

        return self.financial_service.get_cash_flow(symbol)