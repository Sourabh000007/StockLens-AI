from app.rag.keyword_search import KeywordSearch
from app.rag.retrieval_service import RetrievalService
from app.rag.reranker import Reranker


class HybridRetrievalService:
    """
    Combines vector retrieval and keyword retrieval.
    """

    def __init__(self):

        self.vector_retrieval = RetrievalService()

        self.keyword_search = KeywordSearch()

        self.reranker = Reranker()

    def retrieve(
        self,
        question: str,
        company: str,
        report_year: int,
    ):

        vector_chunks = self.vector_retrieval.retrieve(
            question=question,
            company=company,
            report_year=report_year,
        )

        keyword_chunks = self.keyword_search.search(
            question=question,
            chunks=vector_chunks,
            top_k=5,
        )

        merged = {}

        for chunk in vector_chunks:
            merged[chunk.chunk_id] = chunk

        for chunk in keyword_chunks:
            merged[chunk.chunk_id] = chunk

        merged_chunks = list(merged.values())

        return self.reranker.rerank(
            merged_chunks,
            top_k=5,
        )