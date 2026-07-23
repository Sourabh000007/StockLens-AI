from pathlib import Path
from app.core.logger import logger

from app.rag.chunker import TextChunker
from app.rag.embedding_service import EmbeddingService
from app.rag.parser import AnnualReportParser
from app.rag.vector_store import VectorStore
from app.rag.report_cache import ReportCache


class DocumentIndexingService:
    """
    Indexes an annual report into the vector database.
    """

    def __init__(self):

        self.parser = AnnualReportParser()

        self.chunker = TextChunker()

        self.embedding_service = EmbeddingService()

        self.vector_store = VectorStore()

        self.cache = ReportCache()

    def index(self,pdf_path: Path):

        company = pdf_path.parent.name

        report_year = int(pdf_path.stem.split("_")[-1])

        if self.vector_store.is_indexed(
            company,
            report_year,
        ):
            logger.info(
                "Report already indexed. Skipping indexing."
            )

            return 0

        if self.cache.exists(company,report_year):
            text = self.cache.load(company,report_year)

        else:
            text = self.parser.parse(pdf_path)

            self.cache.save(
                company,
                report_year,
                text,
            )

        chunks = self.chunker.split(
            text=text,
            company=company,
            report_year=report_year,
        )

        embeddings = self.embedding_service.embed_chunks(chunks)

        self.vector_store.add_chunks(chunks,embeddings)

        return len(chunks)