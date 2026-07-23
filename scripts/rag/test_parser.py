from pathlib import Path

from app.rag.parser import AnnualReportParser


parser = AnnualReportParser()

text = parser.parse(
    Path(
        "data/reports/TCS/annual_report_2025.pdf"
    )
)

print("=" * 100)

print(f"Characters : {len(text):,}")

print(f"Lines      : {len(text.splitlines()):,}")

print("=" * 100)

print()

print(text[:3000])