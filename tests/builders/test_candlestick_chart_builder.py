from datetime import date

from plotly.graph_objects import Figure

from app.builders.candlestick_chart_builder import CandlestickChartBuilder
from app.models.chart_data import ChartData


def test_build_candlestick_chart():
    chart_data = ChartData(
        dates=[date(2025, 1, 1), date(2025, 1, 2)],
        opens=[100, 105],
        highs=[110, 112],
        lows=[95, 103],
        closes=[108, 111],
        volumes=[1000, 1200],
    )

    figure = CandlestickChartBuilder.build(chart_data)

    assert isinstance(figure, Figure)
    assert len(figure.data) == 1