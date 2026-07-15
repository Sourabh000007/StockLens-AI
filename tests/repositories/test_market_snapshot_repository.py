from app.repositories.market_repository import MarketRepository


def test_get_market_snapshot():

    repository = MarketRepository()

    snapshot = repository.get_market_snapshot("TCS.NS")

    assert snapshot.current_price > 0
    assert snapshot.previous_close > 0
    assert snapshot.currency != ""