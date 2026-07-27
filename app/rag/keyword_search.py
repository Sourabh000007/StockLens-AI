from app.models.rag import RetrievedChunk


class KeywordSearch:
    """
    Performs keyword-based retrieval.
    """

    def search(
        self,
        question: str,
        chunks: list[RetrievedChunk],
        top_k: int = 5,
    ) -> list[RetrievedChunk]:

        keywords = {
            word.lower()
            for word in question.split()
            if len(word) > 2
        }

        scored = []

        for chunk in chunks:

            text = chunk.text.lower()

            score = sum(
                keyword in text
                for keyword in keywords
            )

            scored.append(
                (
                    score,
                    chunk,
                )
            )

        scored.sort(
            reverse=True,
            key=lambda item: item[0],
        )

        return [
            chunk
            for score, chunk in scored
            if score > 0
        ][:top_k]