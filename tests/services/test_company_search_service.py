from app.repositories.company_repository import CompanyRepository
from app.services.company_search_service import CompanySearchService


def test_get_company():
    repository = CompanyRepository()
    service = CompanySearchService(repository)

    company = service.get_company("TCS.NS")

    assert company.symbol == "TCS.NS"
    assert company.company_name != ""