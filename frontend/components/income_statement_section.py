import streamlit as st

from app.builders.revenue_chart_builder import RevenueChartBuilder
from app.models.income_statement import IncomeStatement
from app.transformers.income_statement_transformer import IncomeStatementTransformer


def render_income_statement_section(statement: IncomeStatement):

    """
    Render the income statement section.
    """

    st.subheader("💰 Income Statement")

    chart_data = (
        IncomeStatementTransformer.to_revenue_chart_data(statement)
    )

    figure = RevenueChartBuilder.build(chart_data)

    st.plotly_chart(figure,width="stretch")

    net_income_chart_data = (IncomeStatementTransformer.to_net_income_chart_data(statement))
    net_income_figure = RevenueChartBuilder.build(net_income_chart_data)

    st.plotly_chart(net_income_figure,width="stretch")


    operating_income_chart_data = (IncomeStatementTransformer.to_operating_income_chart_data(statement))
    operating_income_figure = RevenueChartBuilder.build(operating_income_chart_data)
    
    st.plotly_chart(operating_income_figure,width="stretch")