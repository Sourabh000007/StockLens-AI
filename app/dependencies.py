from app.repositories.company_repository import CompanyRepository
from app.services.company_search_service import CompanySearchService

from app.repositories.financial_repository import FinancialRepository
from app.services.financial_service import FinancialService

from app.repositories.market_repository import MarketRepository
from app.services.market_service import MarketService

from frontend.services.company_dashboard_service import CompanyDashboardService

import streamlit as st



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

def get_market_service() -> MarketService:
    """
    Create and return a MarketService instance.
    """
    repository = MarketRepository()
    return MarketService(repository)

@st.cache_resource
def get_company_dashboard_service() -> CompanyDashboardService:
    """
    Create and cache the CompanyDashboardService.
    """
    return CompanyDashboardService()