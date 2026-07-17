from app.repositories.company_repository import CompanyRepository
from app.services.company_search_service import CompanySearchService
from app.models.company_statistics import CompanyStatistics


class CompanyDashboardService:
    """Coordinates company data for the frontend."""

    def __init__(self):
        repository = CompanyRepository()
        self.company_service = CompanySearchService(repository)

    def get_company(self, symbol: str):
        return self.company_service.get_company(symbol)
    
    def get_company_statistics(self,symbol: str) -> CompanyStatistics:
        """
        Retrieve company statistics.
        """

        return self.company_service.get_company_statistics(symbol)