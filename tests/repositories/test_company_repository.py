from app.repositories.company_repository import CompanyRepository


def test_get_company_info():
    repo = CompanyRepository()

    company = repo.get_company_info("TCS.NS")

    assert company.symbol == "TCS.NS"
    assert company.company_name != ""

    assert company.website is not None
    assert company.country is not None
    assert company.city is not None
    assert company.business_summary is not None
    assert company.full_time_employees is None or company.full_time_employees > 0