from pathlib import Path

from app.core.config import settings
from app.core.logger import logger


class ReportCache:
    """
    Handles caching of parsed annual reports.
    """

    def _cache_path(self,company: str,report_year: int) -> Path:

        return (
            settings.cache_path
            / company
            / f"annual_report_{report_year}.md"
        )
    
    def exists(self,company: str,report_year: int) -> bool:

        return self._cache_path(company,report_year).exists()
    
    def load(self,company: str,report_year: int) -> str:

        logger.info(
            "Loading cached report for {} ({})",
            company,
            report_year,
        )

        path = self._cache_path(
            company,
            report_year,
        )

        return path.read_text(
            encoding="utf-8",
        )
    
    def save(self,company: str,report_year: int,text: str):

        logger.info(
            "Saving parsed report to cache for {} ({})",
            company,
            report_year,
        )

        path = self._cache_path(
            company,
            report_year,
        )

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            text,
            encoding="utf-8",
        )