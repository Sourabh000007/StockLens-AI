from app.repositories.company_repository import CompanyRepository
from app.services.company_search_service import CompanySearchService


def test_get_company_statistics():

    repository = CompanyRepository()
    service = CompanySearchService(repository)

    stats = service.get_company_statistics("TCS.NS")

    assert stats.market_cap is not None