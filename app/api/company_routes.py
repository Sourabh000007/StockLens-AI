from fastapi import APIRouter, Depends, HTTPException

from app.core.logger import logger
from app.dependencies import get_company_service
from app.services.company_search_service import CompanySearchService
from app.exceptions.company_not_found import CompanyNotFoundError
from app.models.company import Company

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)

@router.get("/{symbol}", response_model=Company)
def get_company(
    symbol: str,
    service: CompanySearchService = Depends(get_company_service),
):
    """
    Get company information using a Yahoo Finance ticker.
    """

    logger.info("Received request for company: {}", symbol)

    try:
        return service.get_company(symbol)

    except CompanyNotFoundError as error:
        logger.warning(error)
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )