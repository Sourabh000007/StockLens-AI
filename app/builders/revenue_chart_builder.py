import plotly.graph_objects as go

from app.models.financial_chart_data import FinancialChartData


class RevenueChartBuilder:

    @staticmethod
    def build(
        chart_data: FinancialChartData,
    ):
        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=chart_data.x,
                y=chart_data.y,
                mode="lines+markers",
                name="Revenue",
            )
        )

        fig.update_layout(
            title=chart_data.title,
            xaxis_title="Year",
            yaxis_title=chart_data.y_axis_title,
            template="plotly_white",
        )

        return fig