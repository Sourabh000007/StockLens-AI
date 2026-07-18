import streamlit as st

from app.models.balance_sheet import BalanceSheet

from app.builders.revenue_chart_builder import RevenueChartBuilder
from app.transformers.balance_sheet_transformer import (
    BalanceSheetTransformer,
)


def render_balance_sheet_section(statement: BalanceSheet):
    """
    Render the balance sheet section.
    """

    st.markdown("### 🏦 Balance Sheet")

    # -----------------------------
    # Assets & Liabilities
    # -----------------------------

    st.markdown("#### 📊 Assets & Liabilities")

    assets_chart_data = (
        BalanceSheetTransformer.to_total_assets_chart_data(statement)
    )

    assets_figure = RevenueChartBuilder.build(
        assets_chart_data
    )

    liabilities_chart_data = (
        BalanceSheetTransformer.to_total_liabilities_chart_data(statement)
    )

    liabilities_figure = RevenueChartBuilder.build(
        liabilities_chart_data
    )

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            assets_figure,
            width="stretch",
        )

    with col2:
        st.plotly_chart(
            liabilities_figure,
            width="stretch",
        )

    # -----------------------------
    # Shareholders' Equity
    # -----------------------------

    st.markdown("#### 📈 Shareholders' Equity")

    equity_chart_data = (
        BalanceSheetTransformer.to_total_equity_chart_data(statement)
    )

    equity_figure = RevenueChartBuilder.build(
        equity_chart_data
    )

    st.plotly_chart(
        equity_figure,
        width="stretch",
    )