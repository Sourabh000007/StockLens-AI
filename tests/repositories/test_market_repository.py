from app.repositories.market_repository import MarketRepository


def test_get_price_history():
    repository = MarketRepository()

    history = repository.get_price_history("TCS.NS")

    assert len(history) > 0