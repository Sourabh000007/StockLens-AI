from dataclasses import dataclass


@dataclass
class TextChunk:
    """
    Represents one chunk of an annual report.
    """

    id: str

    chunk_id: int

    company: str

    report_year: int

    text: str

class TextChunker:
    """
    Splits document text into overlapping chunks.
    """

    def __init__(self,chunk_size: int = 1000,chunk_overlap: int = 200):

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self,text: str,company: str,report_year: int,) -> list[TextChunk]:

        chunks = []

        start = 0

        chunk_id = 1

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(
                TextChunk(
                    id=f"{company}_{report_year}_{chunk_id:04d}",
                    chunk_id=chunk_id,
                    company=company,
                    report_year=report_year,
                    text=chunk,
                )
            )

            start += (
                self.chunk_size
                - self.chunk_overlap
            )

            chunk_id += 1

        return chunks