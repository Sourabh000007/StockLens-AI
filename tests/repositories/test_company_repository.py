from app.repositories.company_repository import CompanyRepository


def test_get_company_info():
    repo = CompanyRepository()

    company = repo.get_company_info("TCS.NS")

    assert company.symbol == "TCS.NS"
    assert company.company_name != ""