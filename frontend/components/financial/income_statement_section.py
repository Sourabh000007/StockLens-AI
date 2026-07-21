import streamlit as st

from app.builders.revenue_chart_builder import RevenueChartBuilder
from app.models.income_statement import IncomeStatement
from app.transformers.income_statement_transformer import (
    IncomeStatementTransformer,
)


def render_income_statement_section(statement: IncomeStatement):
    """
    Render the income statement section.
    """

    st.markdown("### 💰 Income Statement")

    # -----------------------------
    # Revenue Trend
    # -----------------------------

    st.markdown("#### 📈 Revenue Trend")

    revenue_chart_data = (
        IncomeStatementTransformer.to_revenue_chart_data(statement)
    )

    revenue_figure = RevenueChartBuilder.build(revenue_chart_data)

    st.plotly_chart(
        revenue_figure,
        width="stretch",
    )

    # -----------------------------
    # Profitability
    # -----------------------------

    st.markdown("#### 📊 Profitability")

    net_income_chart_data = (
        IncomeStatementTransformer.to_net_income_chart_data(statement)
    )

    net_income_figure = RevenueChartBuilder.build(net_income_chart_data)

    operating_income_chart_data = (
        IncomeStatementTransformer.to_operating_income_chart_data(statement)
    )

    operating_income_figure = RevenueChartBuilder.build(
        operating_income_chart_data
    )

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            net_income_figure,
            width="stretch",
        )

    with col2:
        st.plotly_chart(
            operating_income_figure,
            width="stretch",
        )