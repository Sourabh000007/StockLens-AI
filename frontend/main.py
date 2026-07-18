import streamlit as st

from frontend.components.header import render_header
from frontend.components.search_bar import render_search_bar
from frontend.components.chart_section import render_chart
from frontend.components.market_snapshot_card import render_market_snapshot
from frontend.components.company_card import render_company_card
from frontend.components.business_summary import render_business_summary
from frontend.components.financial_statement_section import render_financial_statement_section
from frontend.components.company_statistics_card import render_company_statistics_card
from frontend.components.ai_company_summary import render_ai_company_summary
from frontend.components.ai_financial_health import render_ai_financial_health
from frontend.components.ai_strengths import render_ai_strengths
from frontend.components.ai_risks import render_ai_risks
from frontend.components.ai_investment_thesis import render_ai_investment_thesis


from frontend.dependencies import (
    get_market_dashboard_service,
    get_company_dashboard_service,
    get_financial_dashboard_service,
    get_ai_dashboard_service
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

ai_dashboard = get_ai_dashboard_service()


if load_clicked:

    with st.spinner("Loading company information..."):
        company = company_dashboard.get_company(symbol)

        income_statement = financial_dashboard.get_income_statement(symbol)

        cash_flow = financial_dashboard.get_cash_flow(symbol)

        balance_sheet = (financial_dashboard.get_balance_sheet(symbol))

        ai_report = ai_dashboard.get_company_report(
            company=company,
            income_statement=income_statement,
            balance_sheet=balance_sheet,
            cash_flow=cash_flow,
        )

        statistics = company_dashboard.get_company_statistics(symbol)    

        snapshot = market_dashboard.get_market_snapshot(symbol)
        

    render_company_card(company)
    render_business_summary(company)
    render_ai_company_summary(ai_report.summary)
    render_ai_financial_health(ai_report.financial_health)
    render_ai_strengths(ai_report.strengths)
    render_ai_risks(ai_report.risks)
    render_ai_investment_thesis(ai_report.investment_thesis)
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

        

    

    