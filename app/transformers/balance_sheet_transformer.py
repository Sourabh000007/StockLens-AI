from app.models.balance_sheet import BalanceSheet
from app.models.financial_chart_data import FinancialChartData


class BalanceSheetTransformer:

    @staticmethod
    def to_total_assets_chart_data(statement: BalanceSheet) -> FinancialChartData:
        
        """
        Transform the balance sheet into Total Assets chart data.
        """

        return FinancialChartData(
            x=[metric.year for metric in statement.total_assets],
            y=[metric.value for metric in statement.total_assets],
            title="Total Assets Trend",
            y_axis_title="Total Assets",
        )
    
    @staticmethod
    def to_total_liabilities_chart_data(statement: BalanceSheet) -> FinancialChartData:

        """
        Transform the balance sheet into Total Liabilities chart data.
        """

        return FinancialChartData(
            x=[metric.year for metric in statement.total_liabilities],
            y=[metric.value for metric in statement.total_liabilities],
            title="Total Liabilities Trend",
            y_axis_title="Total Liabilities",
        )
    
    @staticmethod
    def to_total_equity_chart_data(
        statement: BalanceSheet,
    ) -> FinancialChartData:
        """
        Transform the balance sheet into Total Equity chart data.
        """

        return FinancialChartData(
            x=[metric.year for metric in statement.total_equity],
            y=[metric.value for metric in statement.total_equity],
            title="Total Equity Trend",
            y_axis_title="Total Equity",
        )