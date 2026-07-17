import streamlit as st

from app.models.cash_flow import CashFlow

from app.builders.revenue_chart_builder import RevenueChartBuilder

from app.transformers.cash_flow_transformer import CashFlowTransformer


def render_cash_flow_section(statement: CashFlow):  
    """
    Render the cash flow section.
    """

    st.subheader("💵 Cash Flow Statement")

    chart_data = (CashFlowTransformer.to_operating_cash_flow_chart_data(statement))
    figure = RevenueChartBuilder.build(chart_data)

    st.plotly_chart(figure,width="stretch")

    investing_chart_data = (CashFlowTransformer.to_investing_cash_flow_chart_data(statement))
    investing_figure = RevenueChartBuilder.build(investing_chart_data)

    st.plotly_chart(investing_figure,width="stretch")

    financing_chart_data = (CashFlowTransformer.to_financing_cash_flow_chart_data(statement))
    financing_figure = RevenueChartBuilder.build(financing_chart_data)

    st.plotly_chart(financing_figure,width="stretch")