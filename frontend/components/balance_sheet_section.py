import streamlit as st

from app.models.balance_sheet import BalanceSheet

from app.builders.revenue_chart_builder import RevenueChartBuilder
from app.transformers.balance_sheet_transformer import (BalanceSheetTransformer)


def render_balance_sheet_section(statement: BalanceSheet):

    """
    Render the balance sheet section.
    """

    st.subheader("🏦 Balance Sheet")

    st.dataframe(
        {
            "Year": [metric.year for metric in statement.total_assets],
            "Total Assets": [metric.value for metric in statement.total_assets],
        },
        width="stretch",
        hide_index=True,
    )

    chart_data = (BalanceSheetTransformer.to_total_assets_chart_data(statement))
    figure = RevenueChartBuilder.build(chart_data)

    st.plotly_chart(figure,width="stretch")

    liabilities_chart_data = (BalanceSheetTransformer.to_total_liabilities_chart_data(statement))
    liabilities_figure = RevenueChartBuilder.build(liabilities_chart_data)

    st.plotly_chart(liabilities_figure,width="stretch")

    equity_chart_data = (BalanceSheetTransformer.to_total_equity_chart_data(statement))
    equity_figure = RevenueChartBuilder.build(equity_chart_data)

    st.plotly_chart(equity_figure,width="stretch")