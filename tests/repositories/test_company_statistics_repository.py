from app.repositories.company_repository import CompanyRepository


def test_get_company_statistics():

    repository = CompanyRepository()

    stats = repository.get_company_statistics("TCS.NS")

    assert stats.market_cap is not None