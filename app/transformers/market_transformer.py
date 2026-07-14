from app.models.chart_data import ChartData
from app.models.market_data import PriceData


class MarketTransformer:
    """Transforms market data into chart-ready structures."""

    @staticmethod
    def to_chart_data(history: list[PriceData]) -> ChartData:
        
        return ChartData(
            dates=[item.date for item in history],
            opens=[item.open for item in history],
            highs=[item.high for item in history],
            lows=[item.low for item in history],
            closes=[item.close for item in history],
            volumes=[item.volume for item in history],
        )