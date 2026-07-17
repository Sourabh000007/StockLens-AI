import pandas as pd
import yfinance as yf

from app.core.logger import logger
from app.models.income_statement import FinancialMetric,IncomeStatement
                                         
from app.models.balance_sheet import BalanceSheet

from app.models.cash_flow import CashFlow


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

    def get_balance_sheet(self, symbol: str) -> BalanceSheet:
        """
        Fetch the company's balance sheet.
        """

        logger.info("Fetching balance sheet for {}", symbol)

        try:
            ticker = self._get_ticker(symbol)

            dataframe = ticker.balance_sheet

            if dataframe.empty:
                raise ValueError(
                    f"No balance sheet found for '{symbol}'."
                )

            return BalanceSheet(
                total_assets=self._extract_metric(
                    dataframe,
                    "Total Assets",
                ),
                total_liabilities=self._extract_metric(
                    dataframe,
                    "Total Liabilities Net Minority Interest",
                ),
                total_equity=self._extract_metric(
                    dataframe,
                    "Stockholders Equity",
                ),
                cash_and_cash_equivalents=self._extract_metric(
                    dataframe,
                    "Cash And Cash Equivalents",
                ),
            )

        except Exception:
            logger.exception(
                "Failed to fetch balance sheet for {}",
                symbol,
            )
            raise

    def get_cash_flow(self,symbol: str) -> CashFlow:
        """
        Fetch the company's cash flow statement.
        """

        logger.info("Fetching cash flow statement for {}", symbol)

        try:
            ticker = self._get_ticker(symbol)

            dataframe = ticker.cash_flow

            if dataframe.empty:
                raise ValueError(
                    f"No cash flow statement found for '{symbol}'."
                )

            return CashFlow(
                operating_cash_flow=self._extract_metric(
                    dataframe,
                    "Operating Cash Flow",
                ),
                investing_cash_flow=self._extract_metric(
                    dataframe,
                    "Investing Cash Flow",
                ),
                financing_cash_flow=self._extract_metric(
                    dataframe,
                    "Financing Cash Flow",
                ),
            )

        except Exception:
            logger.exception(
                "Failed to fetch cash flow statement for {}",
                symbol,
            )
            raise