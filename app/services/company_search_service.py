from app.models.company import Company
from app.models.company_statistics import CompanyStatistics
from app.repositories.company_repository import CompanyRepository


class CompanySearchService:
    """Business logic for company search."""

    def __init__(self, repository: CompanyRepository):
        self.repository = repository

    def get_company(self, symbol: str) -> Company:
        """
        Retrieve company information.

        Args:
            symbol: Yahoo Finance ticker (e.g. TCS.NS)

        Returns:
            Company
        """
        return self.repository.get_company_info(symbol)
    
    def get_company_statistics(self,symbol: str) -> CompanyStatistics:
        """
        Retrieve company statistic information.

        Args:
            symbol: Yahoo Finance ticker (e.g. TCS.NS)

        Returns:
            CompanyStatistics
        """

        return self.repository.get_company_statistics(symbol)