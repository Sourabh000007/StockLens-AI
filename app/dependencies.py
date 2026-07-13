from app.repositories.company_repository import CompanyRepository
from app.services.company_search_service import CompanySearchService

from app.repositories.financial_repository import FinancialRepository
from app.services.financial_service import FinancialService


def get_company_service() -> CompanySearchService:
    """
    Create and return a CompanySearchService instance.
    """
    repository = CompanyRepository()
    return CompanySearchService(repository)

def get_financial_service() -> FinancialService:
    """
    Create and return a FinancialService instance.
    """
    repository = FinancialRepository()
    return FinancialService(repository)