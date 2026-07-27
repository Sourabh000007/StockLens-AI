from app.models.rag import RetrievedChunk


class Reranker:
    """
    Refines retrieved chunks before sending them to the LLM.
    """

    def rerank(
        self,
        chunks: list[RetrievedChunk],
        top_k: int = 5,
    ) -> list[RetrievedChunk]:

        ranked = sorted(
            chunks,
            key=lambda chunk: chunk.distance,
        )

        return ranked[:top_k]