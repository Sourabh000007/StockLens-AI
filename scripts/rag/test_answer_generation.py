from app.rag.answer_generation_service import (
    AnswerGenerationService,
)


def main():

    service = AnswerGenerationService()

    answer = service.ask(
        question="What are TCS's AI initiatives?",
        company="TCS",
        report_year=2025,
    )

    print("=" * 80)

    print("ANSWER")

    print("=" * 80)

    print()

    print(answer)


if __name__ == "__main__":
    main()