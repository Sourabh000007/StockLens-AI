from app.builders.candlestick_chart_builder import CandlestickChartBuilder

from app.transformers.market_transformer import MarketTransformer

from app.services.market_service import MarketService

from app.repositories.market_repository import MarketRepository

from app.models.market_snapshot import MarketSnapshot




class MarketDashboardService:

    def __init__(self):
        repository = MarketRepository()
        self.market_service = MarketService(repository)

    def build_candlestick_chart(
        self,
        symbol: str,
        period: str,
    ):
        history = self.market_service.get_price_history(
            symbol=symbol,
            period=period,
        )

        chart_data = MarketTransformer.to_chart_data(history)

        return CandlestickChartBuilder.build(chart_data)
    
    def get_market_snapshot(self, symbol: str) -> MarketSnapshot:
        """
        Retrieve the latest market snapshot.
        """

        return self.market_service.get_market_snapshot(symbol)
    