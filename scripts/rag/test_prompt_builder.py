from app.ai.rag.answer_prompt_builder import AnswerPromptBuilder


def main():

    builder = AnswerPromptBuilder()

    prompt = builder.build(
        question="What are TCS AI initiatives?",
        context=[
            "TCS has democratized AI access...",
            "TCS launched AI platforms...",
        ],
    )

    print(prompt)


if __name__ == "__main__":
    main()