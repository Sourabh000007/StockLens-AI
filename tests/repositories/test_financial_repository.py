from app.repositories.financial_repository import FinancialRepository


def test_get_income_statement():
    repository = FinancialRepository()

    statement = repository.get_income_statement("TCS.NS")

    assert len(statement.revenue) > 0