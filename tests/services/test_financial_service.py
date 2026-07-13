from app.repositories.financial_repository import FinancialRepository
from app.services.financial_service import FinancialService


def test_get_income_statement():
    repository = FinancialRepository()
    service = FinancialService(repository)

    statement = service.get_income_statement("TCS.NS")

    assert len(statement.revenue) > 0

def test_get_balance_sheet():
    repository = FinancialRepository()
    service = FinancialService(repository)

    statement = service.get_balance_sheet("TCS.NS")

    assert len(statement.total_assets) > 0