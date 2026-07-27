from chromadb import PersistentClient

from app.core.config import settings
from app.models.rag import RetrievedChunk
from app.rag.chunker import TextChunk


class VectorStore:
    """
    Handles storage of document embeddings.
    """

    def __init__(self):

        client = PersistentClient(
            path=str(settings.vector_db_path)
        )

        self.collection = client.get_or_create_collection(
            name="annual_reports"
        )

    def add_chunks(
        self,
        chunks: list[TextChunk],
        embeddings: list[list[float]],
    ):

        self.collection.add(
            ids=[
                chunk.id
                for chunk in chunks
            ],
            documents=[
                chunk.text
                for chunk in chunks
            ],
            embeddings=embeddings,
            metadatas=[
                {
                    "company": chunk.company,
                    "report_year": chunk.report_year,
                    "chunk_id": chunk.chunk_id,
                    "page_number": chunk.page_number if chunk.page_number is not None else -1,
                    "section_title": chunk.section_title or "",
                }
                for chunk in chunks
            ],
        )

    def count(self) -> int:
        """
        Return total stored chunks.
        """

        return self.collection.count()

    def is_indexed(
        self,
        company: str,
        report_year: int,
    ) -> bool:
        """
        Returns True if the report has already been indexed.
        """

        first_chunk_id = (
            f"{company}_{report_year}_0001"
        )

        results = self.collection.get(
            ids=[first_chunk_id]
        )

        return bool(results["ids"])

    def search(
        self,
        query_embedding: list[float],
        company: str,
        report_year: int,
        top_k: int = 5,
    ) -> list[RetrievedChunk]:
        """
        Search for the most relevant chunks.
        """

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where={
                "$and": [
                    {"company": company},
                    {"report_year": report_year},
                ]
            },
            include=[
                "documents",
                "metadatas",
                "distances",
            ],
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        ids = results["ids"][0]
        distances = results["distances"][0]

        retrieved_chunks = []

        for chunk_id, text, metadata, distance in zip(
            ids,
            documents,
            metadatas,
            distances,
        ):

            retrieved_chunks.append(
                RetrievedChunk(
                    chunk_id=chunk_id,
                    text=text,
                    company=metadata["company"],
                    report_year=metadata["report_year"],
                    distance=distance,
                    page_number=(
                        metadata["page_number"]
                        if metadata.get("page_number", -1) != -1
                        else None
                    ),
                    section_title=(
                        metadata["section_title"]
                        if metadata.get("section_title")
                        else None
                    ),
                )
            )

        return retrieved_chunks