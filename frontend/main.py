import streamlit as st

from frontend.components.shared.header import render_header
from frontend.components.shared.search_bar import render_search_bar
from frontend.components.market.chart_section import render_chart
from frontend.components.market.market_snapshot_card import render_market_snapshot
from frontend.components.company.business_summary import render_business_summary
from frontend.components.financial.financial_statement_section import (
    render_financial_statement_section,
)
from frontend.components.company.company_statistics_card import (
    render_company_statistics_card,
)
from frontend.components.ai.ai_company_summary import render_ai_company_summary
from frontend.components.ai.ai_financial_health import render_ai_financial_health
from frontend.components.ai.ai_strengths import render_ai_strengths
from frontend.components.ai.ai_risks import render_ai_risks
from frontend.components.ai.ai_investment_thesis import (
    render_ai_investment_thesis,
)
from frontend.components.news.news_card import render_news_card
from frontend.components.ai.ai_news_summary import render_ai_news_summary
from frontend.components.company.company_hero import render_company_hero

from frontend.components.ai.company_health_score import (
    render_company_health_score,
)

from frontend.dependencies import (
    get_market_dashboard_service,
    get_company_dashboard_service,
    get_financial_dashboard_service,
    get_ai_dashboard_service,
    get_news_dashboard_service,
)


st.set_page_config(
    page_title="StockLens AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.write("")

render_header()

with st.container():
    symbol, period, load_clicked = render_search_bar()

st.write("")

market_dashboard = get_market_dashboard_service()
company_dashboard = get_company_dashboard_service()
financial_dashboard = get_financial_dashboard_service()
news_dashboard = get_news_dashboard_service()
ai_dashboard = get_ai_dashboard_service()

if load_clicked:

    with st.status("Preparing analysis...", expanded=True) as status:

        status.write("📥 Fetching company profile...")
        company = company_dashboard.get_company(symbol)

        status.write("📈 Loading financial statements...")
        income_statement = financial_dashboard.get_income_statement(symbol)
        cash_flow = financial_dashboard.get_cash_flow(symbol)
        balance_sheet = financial_dashboard.get_balance_sheet(symbol)

        status.write("📰 Fetching latest news...")
        news_articles = news_dashboard.get_news(symbol)

        status.write("📊 Loading market statistics...")
        statistics = company_dashboard.get_company_statistics(symbol)
        snapshot = market_dashboard.get_market_snapshot(symbol)

        status.write("🤖 Generating AI research report...")
        ai_report = ai_dashboard.get_company_report(
            company=company,
            income_statement=income_statement,
            balance_sheet=balance_sheet,
            cash_flow=cash_flow,
            news_articles=news_articles,
        )

        status.write("📉 Building candlestick chart...")
        figure = market_dashboard.build_candlestick_chart(
            symbol=symbol,
            period=period,
        )

        status.update(
            label="✅ Analysis complete!",
            state="complete",
            expanded=False,
        )

            # ----------------------------------------------------
    # Company Overview
    # ----------------------------------------------------

    with st.container(border=True):

        render_company_hero(company)

        st.divider()

        render_company_health_score(ai_report)

        st.divider()

        render_business_summary(company)

    # ----------------------------------------------------
    # AI Research Report
    # ----------------------------------------------------

    with st.container(border=True):

        st.subheader("🤖 AI Research Report")

        st.caption(
            "AI-generated analysis based on company fundamentals, financial statements, and recent news."
        )

        st.divider()

        render_ai_company_summary(ai_report.summary)
        render_ai_news_summary(ai_report.news_summary)
        render_ai_financial_health(ai_report.financial_health)
        render_ai_strengths(ai_report.strengths)
        render_ai_risks(ai_report.risks)
        render_ai_investment_thesis(ai_report.investment_thesis)

    # ----------------------------------------------------
    # Market Snapshot + Key Statistics
    # ----------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            render_market_snapshot(snapshot)

    with col2:
        with st.container(border=True):
            render_company_statistics_card(statistics)

    # ----------------------------------------------------
    # Price Chart
    # ----------------------------------------------------

    with st.container(border=True):
        render_chart(figure)

    # ----------------------------------------------------
    # Financial Statements
    # ----------------------------------------------------

    st.markdown("###")

    render_financial_statement_section(
        income_statement,
        balance_sheet,
        cash_flow,
    )

    # ----------------------------------------------------
    # Latest Company News
    # ----------------------------------------------------

    with st.container(border=True):
        render_news_card(news_articles)