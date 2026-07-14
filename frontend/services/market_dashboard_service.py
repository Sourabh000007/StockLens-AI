from app.builders.candlestick_chart_builder import (
    CandlestickChartBuilder,
)

from app.transformers.market_transformer import MarketTransformer
from app.services.market_service import MarketService
from app.repositories.market_repository import MarketRepository

class MarketDashboardService:

    def __init__(self):
        repository = MarketRepository()
        self.market_service = MarketService(repository)

    def build_candlestick_chart(
        self,
        symbol: str,
        period: str = "1y",
    ):
        history = self.market_service.get_price_history(
            symbol,
            period,
        )

        chart_data = MarketTransformer.to_chart_data(history)

        return CandlestickChartBuilder.build(chart_data)