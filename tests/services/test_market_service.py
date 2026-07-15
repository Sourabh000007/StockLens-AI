from app.repositories.market_repository import MarketRepository
from app.services.market_service import MarketService


def test_get_price_history():
    repository = MarketRepository()
    service = MarketService(repository)

    history = service.get_price_history("TCS.NS")

    assert len(history) > 0


def test_get_market_snapshot():
    repository = MarketRepository()
    service = MarketService(repository)

    snapshot = service.get_market_snapshot("TCS.NS")

    assert snapshot.current_price > 0
    assert snapshot.market_cap > 0