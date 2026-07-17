from app.models.cash_flow import CashFlow
from app.models.financial_chart_data import FinancialChartData


class CashFlowTransformer:

    @staticmethod
    def to_operating_cash_flow_chart_data(statement: CashFlow) -> FinancialChartData:
        """
        Transform the cash flow statement into operating cash flow chart data.
        """

        return FinancialChartData(
            x=[metric.year for metric in statement.operating_cash_flow],
            y=[metric.value for metric in statement.operating_cash_flow],
            title="Operating Cash Flow Trend",
            y_axis_title="Operating Cash Flow",
        )
    
    @staticmethod
    def to_investing_cash_flow_chart_data(statement: CashFlow) -> FinancialChartData:
        """
        Transform the cash flow statement into investing cash flow chart data.
        """

        return FinancialChartData(
            x=[metric.year for metric in statement.investing_cash_flow],
            y=[metric.value for metric in statement.investing_cash_flow],
            title="Investing Cash Flow Trend",
            y_axis_title="Investing Cash Flow",
        )
    
    @staticmethod
    def to_financing_cash_flow_chart_data(statement: CashFlow) -> FinancialChartData:
        """
        Transform the cash flow statement into financing cash flow chart data.
        """

        return FinancialChartData(
            x=[metric.year for metric in statement.financing_cash_flow],
            y=[metric.value for metric in statement.financing_cash_flow],
            title="Financing Cash Flow Trend",
            y_axis_title="Financing Cash Flow",
        )