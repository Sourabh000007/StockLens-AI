import streamlit as st

from frontend.services.market_dashboard_service import MarketDashboardService
from frontend.services.company_dashboard_service import CompanyDashboardService




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