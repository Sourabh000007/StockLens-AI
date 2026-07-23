from pathlib import Path

from app.rag.chunker import TextChunker
from app.rag.parser import AnnualReportParser


parser = AnnualReportParser()

text = parser.parse(
    Path(
        "data/reports/TCS/annual_report_2025.pdf"
    )
)

chunker = TextChunker()

chunks = chunker.split(text)

print(f"Total Chunks : {len(chunks)}")

print()

print(chunks[0])

print()

print(chunks[1])