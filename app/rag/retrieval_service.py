from app.models.rag import RetrievedChunk
from app.rag.embedding_service import EmbeddingService
from app.rag.vector_store import VectorStore
from app.rag.reranker import Reranker


class RetrievalService:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.vector_store = VectorStore()

        self.reranker = Reranker()

    def retrieve(
        self,
        question: str,
        company: str,
        report_year: int,
    ) -> list[RetrievedChunk]:
        """
        Retrieve the most relevant chunks.
        """

        query_embedding = self.embedding_service.embed_query(
            question,
        )

        chunks = self.vector_store.search(
            query_embedding=query_embedding,
            company=company,
            report_year=report_year,
            top_k=15,
        )

        return self.reranker.rerank(chunks)