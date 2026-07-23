from app.core.config import settings
from app.rag.document_indexing_service import DocumentIndexingService


def main():
    pdf_path = (
        settings.report_path
        / "TCS"
        / "annual_report_2025.pdf"
    )

    company = pdf_path.parent.name
    report_year = pdf_path.stem.split("_")[-1]

    indexing_service = DocumentIndexingService()

    total_chunks = indexing_service.index(pdf_path)

    print("=" * 80)
    print("Document Indexed Successfully")
    print(f"Company      : {company}")
    print(f"Report Year  : {report_year}")
    if total_chunks == 0:
        print("Already Indexed")
    else:
        print(f"Total Chunks : {total_chunks}")
        print("=" * 80)


if __name__ == "__main__":
    main()