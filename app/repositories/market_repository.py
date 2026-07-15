import yfinance as yf

from app.core.logger import logger
from app.models.market_data import PriceData
# from datetime import date

from app.models.market_snapshot import MarketSnapshot

class MarketRepository:
    """Repository responsible for fetching market data."""

    def _get_ticker(self, symbol: str) -> yf.Ticker:
        """
        Create and return a Yahoo Finance ticker object.
        """
        return yf.Ticker(symbol)
    
    def get_price_history(self,symbol: str,period: str = "1y") -> list[PriceData]:

        """
        Fetch historical OHLCV data for a company.
        """

        logger.info("Fetching price history for {} (period={})",symbol,period)

        try:
            ticker = self._get_ticker(symbol)

            dataframe = ticker.history(period=period)

            if dataframe.empty:
                raise ValueError(
                    f"No market data found for '{symbol}'."
                )

            history: list[PriceData] = []

            for index, row in dataframe.iterrows():
                history.append(
                    PriceData(
                        date=index.date(),
                        open=float(row["Open"]),
                        high=float(row["High"]),
                        low=float(row["Low"]),
                        close=float(row["Close"]),
                        volume=int(row["Volume"]),
                    )
                )

            return history

        except Exception:
            logger.exception(
                "Failed to fetch market history for {}",
                symbol,
            )
            raise

    def get_market_snapshot(self, symbol: str) -> MarketSnapshot:
        """
        Fetch the latest market snapshot for a company.
        """

        try:
            ticker = yf.Ticker(symbol)

            info = ticker.info

            return MarketSnapshot(
                current_price=info.get("currentPrice", 0.0),
                previous_close=info.get("previousClose", 0.0),
                day_high=info.get("dayHigh", 0.0),
                day_low=info.get("dayLow", 0.0),
                volume=info.get("volume", 0),
                market_cap=info.get("marketCap", 0.0),
                currency=info.get("currency", ""),
            )

        except Exception as ex:
            logger.exception(
                "Failed to fetch market snapshot for %s",
                symbol,
            )

            raise RuntimeError(
                f"Unable to fetch market snapshot for '{symbol}'."
            ) from ex