from sentence_transformers import SentenceTransformer

from app.rag.chunker import TextChunk
from app.core.config import settings


class EmbeddingService:
    """
    Generates embeddings for document chunks.
    """

    def __init__(self):

        self.model = SentenceTransformer(settings.embedding_model)

    def embed_chunk(self,chunk: TextChunk) -> list[float]:
        """
        Generate an embedding for one chunk.
        """

        embedding = self.model.encode(
            chunk.text,
            normalize_embeddings=True,
        )

        return embedding.tolist()
    
    def embed_chunks(self,chunks: list[TextChunk]) -> list[list[float]]:

        """
        Generate embeddings for multiple chunks.
        """

        return self.model.encode(
            [chunk.text for chunk in chunks],
            normalize_embeddings=True,
        ).tolist()
    
    def embed_query(
        self,
        question: str,
    ) -> list[float]:
        
        """
        Generate an embedding for a user query.
        """

        embedding = self.model.encode(
            question,
            normalize_embeddings=True,
        )

        return embedding.tolist()