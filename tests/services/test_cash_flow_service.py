from app.repositories.financial_repository import FinancialRepository
from app.services.financial_service import FinancialService


def test_get_cash_flow():

    repository = FinancialRepository()
    service = FinancialService(repository)

    statement = service.get_cash_flow("TCS.NS")

    assert len(statement.operating_cash_flow) > 0