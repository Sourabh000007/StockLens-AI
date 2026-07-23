from app.models.rag.retrieved_chunk import RetrievedChunk


class AnswerPromptBuilder:

    def build(
        self,
        question: str,
        context: list[RetrievedChunk],
    ) -> str:

        context_text = "\n\n".join(
            chunk.text
            for chunk in context
        )

        return (
            "You are a senior equity research analyst.\n\n"
            "Answer ONLY using the information provided in the annual report context.\n\n"
            'If the answer cannot be found in the context, respond exactly:\n'
            '"I could not find this information in the annual report."\n\n'
            "Do not make assumptions.\n\n"
            "Annual Report Context\n"
            "---------------------\n\n"
            f"{context_text}\n\n"
            "Question\n"
            "--------\n\n"
            f"{question}\n\n"
            "Answer:"
        )