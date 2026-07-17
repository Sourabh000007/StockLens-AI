from app.models.income_statement import IncomeStatement

from frontend.components.income_statement_section import render_income_statement_section

from app.models.balance_sheet import BalanceSheet
from frontend.components.balance_sheet_section import render_balance_sheet_section

from app.models.cash_flow import CashFlow
from frontend.components.cash_flow_section import render_cash_flow_section


def render_financial_statement_section(
        income_statement: IncomeStatement,
        balance_sheet: BalanceSheet,
        cash_flow: CashFlow,
):

    """
    Render all financial statements.
    """

    render_income_statement_section(income_statement)
    render_balance_sheet_section(balance_sheet)
    render_cash_flow_section(cash_flow)