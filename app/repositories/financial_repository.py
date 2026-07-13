import pandas as pd
import yfinance as yf

from app.core.logger import logger
from app.models.income_statement import (FinancialMetric,IncomeStatement,)


class FinancialRepository:
    """Repository responsible for fetching financial statements."""

    def _get_ticker(self, symbol: str) -> yf.Ticker:
        """
        Create and return a Yahoo Finance ticker object.
        """
        return yf.Ticker(symbol)

    def _extract_metric(self,dataframe: pd.DataFrame,metric_name: str,) -> list[FinancialMetric]:
        """
        Extract a financial metric from a Yahoo Finance dataframe.
        """

        if metric_name not in dataframe.index:
            logger.warning("{} not found.", metric_name)
            return []

        values = dataframe.loc[metric_name]

        metrics = []

        for year, value in values.items():
            metrics.append(
                FinancialMetric(
                    year=str(year.year),
                    value=float(value),
                )
            )

        return metrics
    
    def get_income_statement(self, symbol: str) -> IncomeStatement:
        """
        Fetch the company's income statement.
        """

        logger.info("Fetching income statement for {}", symbol)

        try:
            ticker = self._get_ticker(symbol)

            dataframe = ticker.financials

            if dataframe.empty:
                raise ValueError(
                    f"No income statement found for '{symbol}'."
                )

            return IncomeStatement(
                revenue=self._extract_metric(dataframe, "Total Revenue"),
                gross_profit=self._extract_metric(dataframe, "Gross Profit"),
                operating_income=self._extract_metric(
                    dataframe,
                    "Operating Income",
                ),
                net_income=self._extract_metric(dataframe, "Net Income"),
            )

        except Exception:
            logger.exception(
                "Failed to fetch income statement for {}",
                symbol,
            )
            raise