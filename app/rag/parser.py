from pathlib import Path
import pymupdf4llm

from app.core.logger import logger
from app.rag.text_cleaner import TextCleaner


class AnnualReportParser:
    """
    Parses annual report PDFs into markdown text.
    """

    def __init__(self):

        self.cleaner = TextCleaner()

    def parse(
        self,
        pdf_path: Path,
    ) -> str:
        
        """
        Parse an annual report PDF.
        """

        logger.info(
            "Parsing annual report: {}",
            pdf_path.name,
        )

        markdown = pymupdf4llm.to_markdown(
            str(pdf_path),
        )

        markdown = self.cleaner.clean(markdown)

        logger.info(
            "Annual report parsed successfully."
        )

        return markdown