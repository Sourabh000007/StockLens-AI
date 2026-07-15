from pydantic import BaseModel


class MarketSnapshot(BaseModel):
    """
    Represents the latest market snapshot for a stock.

    This model contains dynamic market data that changes
    throughout the trading session.
    """

    current_price: float
    previous_close: float

    day_high: float
    day_low: float

    volume: int

    market_cap: float

    currency: str