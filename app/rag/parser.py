from pathlib import Path

import fitz
import pymupdf4llm

from app.core.logger import logger
from app.models.rag import ReportPage


class AnnualReportParser:
    """
    Parses annual report PDFs into page-wise markdown.
    """

    def parse(
        self,
        pdf_path: Path,
    ) -> list[ReportPage]:

        logger.info(
            "Parsing annual report: {}",
            pdf_path.name,
        )

        document = fitz.open(pdf_path)

        pages = []

        for page_index in range(len(document)):

            markdown = pymupdf4llm.to_markdown(
                str(pdf_path),
                pages=[page_index],
            )

            pages.append(
                ReportPage(
                    page_number=page_index + 1,
                    text=markdown,
                )
            )

        logger.info(
            "Annual report parsed successfully."
        )

        return pages