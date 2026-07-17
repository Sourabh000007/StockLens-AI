import streamlit as st

from frontend.components.header import render_header
from frontend.components.search_bar import render_search_bar
from frontend.components.chart_section import render_chart
from frontend.components.market_snapshot_card import render_market_snapshot
from frontend.components.company_card import render_company_card
from frontend.components.business_summary import render_business_summary
from frontend.components.financial_statement_section import render_financial_statement_section
from frontend.components.company_statistics_card import render_company_statistics_card

from frontend.dependencies import (
    get_market_dashboard_service,
    get_company_dashboard_service,
    get_financial_dashboard_service
)




st.set_page_config(
    page_title="StockLens AI",
    page_icon="📈",
    layout="wide",
)

render_header()

symbol, period, load_clicked = render_search_bar()

market_dashboard = get_market_dashboard_service()

company_dashboard = get_company_dashboard_service()

financial_dashboard = get_financial_dashboard_service()





if load_clicked:

    with st.spinner("Loading company information..."):
        company = company_dashboard.get_company(symbol)
        statistics = company_dashboard.get_company_statistics(symbol)
        snapshot = market_dashboard.get_market_snapshot(symbol)
        

    render_company_card(company)
    render_business_summary(company)
    render_company_statistics_card(statistics)
    render_market_snapshot(snapshot)

    with st.spinner("Loading market data..."):
        figure = market_dashboard.build_candlestick_chart(
            symbol=symbol,
            period=period,
        )

    render_chart(figure)

    with st.spinner("Loading financial statements..."):
        income_statement = financial_dashboard.get_income_statement(symbol)

        balance_sheet = financial_dashboard.get_balance_sheet(symbol)

        cash_flow = financial_dashboard.get_cash_flow(symbol)

        render_financial_statement_section(income_statement,balance_sheet,cash_flow)

        

    

    