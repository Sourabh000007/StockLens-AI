import plotly.graph_objects as go

from app.models.chart_data import ChartData


class CandlestickChartBuilder:
    """Builds a Plotly candlestick chart."""

    @staticmethod
    def build(chart_data: ChartData) -> go.Figure:
        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=chart_data.dates,
                    open=chart_data.opens,
                    high=chart_data.highs,
                    low=chart_data.lows,
                    close=chart_data.closes,
                    name="OHLC",
                )
            ]
        )

        fig.update_layout(
            title="Stock Price History",
            xaxis_title="Date",
            yaxis_title="Price",
            template="plotly_white",
            xaxis_rangeslider_visible=False,
            height=650,
        )

        return fig