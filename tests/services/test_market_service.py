from app.repositories.market_repository import MarketRepository
from app.services.market_service import MarketService


def test_get_price_history():
    repository = MarketRepository()
    service = MarketService(repository)

    history = service.get_price_history("TCS.NS")

    assert len(history) > 0