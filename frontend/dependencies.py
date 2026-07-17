import streamlit as st

from frontend.services.market_dashboard_service import MarketDashboardService
from frontend.services.company_dashboard_service import CompanyDashboardService

from frontend.services.financial_dashboard_service import FinancialDashboardService

from frontend.services.ai_dashboard_service import AIDashboardService

@st.cache_resource
def get_market_dashboard_service() -> MarketDashboardService:
    """
    Create and cache the MarketDashboardService.
    """
    return MarketDashboardService()

@st.cache_resource
def get_company_dashboard_service() -> CompanyDashboardService:
    """
    Create and cache the CompanyDashboardService.
    """
    return CompanyDashboardService()

@st.cache_resource
def get_financial_dashboard_service() -> FinancialDashboardService:
    """
    Create and cache the FinancialDashboardService.
    """
    return FinancialDashboardService()

@st.cache_resource
def get_ai_dashboard_service() -> AIDashboardService:
    """
    Create and cache the AI dashboard service.
    """

    return AIDashboardService()