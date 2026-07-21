import streamlit as st

from app.models.cash_flow import CashFlow

from app.builders.revenue_chart_builder import RevenueChartBuilder
from app.transformers.cash_flow_transformer import (
    CashFlowTransformer,
)


def render_cash_flow_section(statement: CashFlow):
    """
    Render the cash flow section.
    """

    st.markdown("### 💵 Cash Flow Statement")

    # -----------------------------
    # Operating Cash Flow
    # -----------------------------

    st.markdown("#### 💰 Operating Cash Flow")

    operating_chart_data = (
        CashFlowTransformer.to_operating_cash_flow_chart_data(statement)
    )

    operating_figure = RevenueChartBuilder.build(
        operating_chart_data
    )

    st.plotly_chart(
        operating_figure,
        width="stretch",
    )

    # -----------------------------
    # Investing & Financing
    # -----------------------------

    st.markdown("#### 🔄 Cash Movements")

    investing_chart_data = (
        CashFlowTransformer.to_investing_cash_flow_chart_data(statement)
    )

    investing_figure = RevenueChartBuilder.build(
        investing_chart_data
    )

    financing_chart_data = (
        CashFlowTransformer.to_financing_cash_flow_chart_data(statement)
    )

    financing_figure = RevenueChartBuilder.build(
        financing_chart_data
    )

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            investing_figure,
            width="stretch",
        )

    with col2:
        st.plotly_chart(
            financing_figure,
            width="stretch",
        )