from app.repositories.financial_repository import FinancialRepository


def test_get_balance_sheet():
    repository = FinancialRepository()

    statement = repository.get_balance_sheet("TCS.NS")

    assert len(statement.total_assets) > 0