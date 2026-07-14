from datetime import date

from app.models.market_data import PriceData
from app.transformers.market_transformer import MarketTransformer


def test_to_chart_data():
    history = [
        PriceData(
            date=date(2025, 1, 1),
            open=100,
            high=110,
            low=95,
            close=105,
            volume=1000,
        ),
        PriceData(
            date=date(2025, 1, 2),
            open=106,
            high=112,
            low=104,
            close=111,
            volume=1200,
        ),
    ]

    chart_data = MarketTransformer.to_chart_data(history)

    assert chart_data.dates == [
        date(2025, 1, 1),
        date(2025, 1, 2),
    ]

    assert chart_data.closes == [105, 111]
    assert chart_data.volumes == [1000, 1200]