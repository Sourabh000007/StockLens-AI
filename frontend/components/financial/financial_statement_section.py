import streamlit as st

from app.models.income_statement import IncomeStatement

from frontend.components.financial.income_statement_section import render_income_statement_section

from app.models.balance_sheet import BalanceSheet
from frontend.components.financial.balance_sheet_section import render_balance_sheet_section

from app.models.cash_flow import CashFlow
from frontend.components.financial.cash_flow_section import render_cash_flow_section


def render_financial_statement_section(income_statement: IncomeStatement,balance_sheet: BalanceSheet,cash_flow: CashFlow):

    """
    Render all financial statements.
    """
    st.header("💰 Financial Statements")
    st.caption("Click a section to explore financial data.")

    with st.expander(
        "📈 Income Statement",
        expanded=True,
    ):
        render_income_statement_section(income_statement)

    with st.expander(
    "📊 Balance Sheet",
    ):
        render_balance_sheet_section(balance_sheet)

    with st.expander(
    "💵 Cash Flow",
    ):
        render_cash_flow_section(cash_flow)