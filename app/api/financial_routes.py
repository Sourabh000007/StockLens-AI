from fastapi import APIRouter, Depends, HTTPException

from app.core.logger import logger
from app.dependencies import get_financial_service
from app.services.financial_service import FinancialService
from app.models.income_statement import IncomeStatement

router = APIRouter(prefix="/financials",tags=["Financials"])


@router.get("/income-statement/{symbol}",response_model=IncomeStatement)

def get_income_statement(
    symbol: str,
    service: FinancialService = Depends(get_financial_service),
):
    """
    Get the company's income statement.
    """

    logger.info("Received request for income statement: {}", symbol)

    try:
        return service.get_income_statement(symbol)

    except Exception as error:
        logger.exception("Failed to retrieve income statement")
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )