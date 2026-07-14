from app.models.market_data import PriceData
from app.repositories.market_repository import MarketRepository


class MarketService:
    """Business logic for market data."""

    def __init__(self, repository: MarketRepository):
        self.repository = repository

    def get_price_history(self,symbol: str,period: str = "1y") -> list[PriceData]:
        
        """
        Retrieve historical market data.
        """
        return self.repository.get_price_history(symbol, period)