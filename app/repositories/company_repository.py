from typing import Any

import yfinance as yf

from app.core.logger import logger
from app.models.company import Company

from app.exceptions.company_not_found import CompanyNotFoundError


class CompanyRepository:
    """Repository responsible for fetching company data from Yahoo Finance."""

    def get_company_info(self, symbol: str) -> Company:
        """
        Fetch company information from Yahoo Finance.

        Args:
            symbol: Yahoo Finance ticker (e.g. TCS.NS)

        Returns:
            Company

        Raises:
            ValueError: If the ticker is invalid or no company data is found.
        """

        logger.info("Fetching company information for {}", symbol)

        try:
            ticker = yf.Ticker(symbol)
            info: dict[str, Any] = ticker.info

            if not info:
                raise CompanyNotFoundError(symbol)

            company_name = info.get("longName")

            if not company_name:
                raise CompanyNotFoundError(symbol)

            return Company(
                symbol=symbol.upper(),
                company_name=company_name,
                exchange=info.get("exchange", "Unknown"),
                sector=info.get("sector", "Unknown"),
                industry=info.get("industry", "Unknown"),
            )

        except CompanyNotFoundError:
            logger.warning("Company not found: {}", symbol)
            raise

        except Exception as error:
            logger.exception("Unexpected error while fetching {}", symbol)
            raise Exception("Internal server error") from error