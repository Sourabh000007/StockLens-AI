from app.models.market_data import PriceData
from app.repositories.market_repository import MarketRepository
from app.models.market_snapshot import MarketSnapshot


class MarketService:
    """Business logic for market data."""

    def __init__(self, repository: MarketRepository):
        self.repository = repository

    def get_price_history(self,symbol: str,period: str = "1y") -> list[PriceData]:
        
        """
        Retrieve historical market data.
        """
        return self.repository.get_price_history(symbol, period)
    
    def get_market_snapshot(self, symbol: str) -> MarketSnapshot:
        """
        Retrieve the latest market snapshot.
        """

        return self.repository.get_market_snapshot(symbol)