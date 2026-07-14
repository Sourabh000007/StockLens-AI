import streamlit as st

from frontend.components.header import render_header
from frontend.components.search_bar import render_search_bar
from frontend.components.chart_section import render_chart
from frontend.dependencies import get_market_dashboard_service,get_company_dashboard_service

from frontend.components.company_card import render_company_card

st.set_page_config(
    page_title="StockLens AI",
    page_icon="📈",
    layout="wide",
)

render_header()

symbol, load_clicked = render_search_bar()

market_dashboard = get_market_dashboard_service()

company_dashboard = get_company_dashboard_service()

if load_clicked:

    with st.spinner("Loading company information..."):
        company = company_dashboard.get_company(symbol)

    render_company_card(company)

    with st.spinner("Loading market data..."):
        figure = market_dashboard.build_candlestick_chart(symbol)

    render_chart(figure)

    