from fastapi import APIRouter, Depends, HTTPException

from app.core.logger import logger
from app.dependencies import get_market_service
from app.models.market_data import PriceData
from app.services.market_service import MarketService

router = APIRouter(prefix="/market",tags=["Market"])


@router.get("/history/{symbol}",response_model=list[PriceData])
def get_price_history(
    symbol: str,
    period: str = "1y",
    service: MarketService = Depends(get_market_service),
):
    """
    Get historical OHLCV market data.
    """

    logger.info(
        "Received request for market history: {} ({})",
        symbol,
        period,
    )

    try:
        return service.get_price_history(symbol, period)

    except Exception as error:
        logger.exception(
            "Failed to retrieve market history for {}",
            symbol,
        )

        raise HTTPException(
            status_code=500,
            detail=str(error),
        )