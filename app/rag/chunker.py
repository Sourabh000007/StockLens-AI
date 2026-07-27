from dataclasses import dataclass
import re


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

    page_number: int | None = None

    section_title: str | None = None

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

        # NEW
        current_page = None

        while start < len(text):
            end = start + self.chunk_size
            chunk = text[start:end]

            page_number = self._find_page_number(chunk)

            # NEW: propagate the last known page
            if page_number is not None:
                current_page = page_number
            else:
                page_number = current_page

            chunks.append(
                TextChunk(
                    id=f"{company}_{report_year}_{chunk_id:04d}",
                    chunk_id=chunk_id,
                    company=company,
                    report_year=report_year,
                    text=chunk,
                    page_number=page_number,
                )
            )

            start += self.chunk_size - self.chunk_overlap
            chunk_id += 1

        return chunks

    def _find_page_number(self,text: str,) -> int | None:
        
        """
        Attempt to detect the annual report page number.
        """

        matches = re.findall(
            r"\n\s*(\d{1,3})\s*\n",
            text,
        )

        if not matches:
            return None

        return int(matches[-1])