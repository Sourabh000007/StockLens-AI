from app.repositories.financial_repository import FinancialRepository


def test_get_cash_flow():

    repository = FinancialRepository()

    statement = repository.get_cash_flow("TCS.NS")

    assert len(statement.operating_cash_flow) > 0
    assert len(statement.investing_cash_flow) > 0
    assert len(statement.financing_cash_flow) > 0