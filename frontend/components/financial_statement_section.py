from app.models.income_statement import IncomeStatement

from frontend.components.income_statement_section import render_income_statement_section


def render_financial_statement_section(income_statement: IncomeStatement):

    """
    Render all financial statements.
    """

    render_income_statement_section(income_statement)