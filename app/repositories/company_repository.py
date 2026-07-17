from typing import Any

import yfinance as yf

from app.core.logger import logger
from app.models.company import Company
from app.models.company_statistics import CompanyStatistics

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
                symbol=info.get("symbol", ""),

                company_name=info.get("longName", ""),
                short_name=info.get("shortName", ""),

                exchange=info.get("exchange", ""),

                sector=info.get("sector", ""),
                industry=info.get("industry", ""),

                country=info.get("country", ""),
                city=info.get("city", ""),

                website=info.get("website", ""),

                investor_relations_website=info.get("irWebsite"),

                full_time_employees=info.get("fullTimeEmployees"),

                business_summary=info.get("longBusinessSummary", ""),
            )

        except CompanyNotFoundError:
            logger.warning("Company not found: {}", symbol)
            raise

        except Exception as error:
            logger.exception("Unexpected error while fetching {}", symbol)
            raise Exception("Internal server error") from error
        

    def get_company_statistics(self,symbol: str) -> CompanyStatistics:
        """
        Fetch company statistics from Yahoo Finance.

        Args:
            symbol: Yahoo Finance ticker (e.g. TCS.NS)

        Returns:
            CompanyStatistics
        """

        logger.info("Fetching company statistics for {}", symbol)

        try:
            ticker = yf.Ticker(symbol)
            info: dict[str, Any] = ticker.info

            if not info:
                raise CompanyNotFoundError(symbol)

            return CompanyStatistics(
                market_cap=info.get("marketCap"),
                enterprise_value=info.get("enterpriseValue"),

                trailing_pe=info.get("trailingPE"),
                forward_pe=info.get("forwardPE"),

                dividend_yield=info.get("dividendYield"),

                beta=info.get("beta"),

                fifty_two_week_high=info.get("fiftyTwoWeekHigh"),
                fifty_two_week_low=info.get("fiftyTwoWeekLow"),
            )

        except CompanyNotFoundError:
            logger.warning("Company statistics not found: {}", symbol)
            raise

        except Exception as error:
            logger.exception(
                "Unexpected error while fetching statistics for {}",
                symbol,
            )
            raise Exception("Internal server error") from error