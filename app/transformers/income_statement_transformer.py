from app.models.financial_chart_data import FinancialChartData
from app.models.income_statement import IncomeStatement


class IncomeStatementTransformer:

    @staticmethod
    def to_revenue_chart_data(statement: IncomeStatement) -> FinancialChartData:

        """
        Transform an income statement into revenue chart data.
        """

        return FinancialChartData(
            x=[metric.year for metric in statement.revenue],
            y=[metric.value for metric in statement.revenue],
            title="Revenue Trend",
            y_axis_title="Revenue",
        )
    
    @staticmethod
    def to_net_income_chart_data(statement: IncomeStatement) -> FinancialChartData:
        """
        Transform an income statement into net income chart data.
        """

        return FinancialChartData(
            x=[metric.year for metric in statement.net_income],
            y=[metric.value for metric in statement.net_income],
            title="Net Income Trend",
            y_axis_title="Net Income",
        )
    
    @staticmethod
    def to_operating_income_chart_data(statement: IncomeStatement) -> FinancialChartData:
        """
        Transform an income statement into operating income chart data.
        """

        return FinancialChartData(
            x=[metric.year for metric in statement.operating_income],
            y=[metric.value for metric in statement.operating_income],
            title="Operating Income Trend",
            y_axis_title="Operating Income",
        )