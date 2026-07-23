from pathlib import Path

from app.services.annual_report_chat_service import AnnualReportChatService


def main():

    company = "TCS"

    report_year = 2025

    service = AnnualReportChatService()

    question = (
        "What are TCS AI initiatives?"
    )

    answer = service.ask(
        company=company,
        report_year=report_year,
        question=question,
    )

    print("=" * 80)
    print("QUESTION")
    print("=" * 80)
    print(question)

    print()

    print("=" * 80)
    print("ANSWER")
    print("=" * 80)

    print(answer)


if __name__ == "__main__":
    main()