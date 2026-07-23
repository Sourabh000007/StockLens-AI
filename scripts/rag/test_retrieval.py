from app.rag.retrieval_service import RetrievalService


def main():

    retrieval = RetrievalService()

    chunks = retrieval.retrieve(
        question="What are TCS's AI initiatives?",
        company="TCS",
        report_year=2025,
    )

    print("=" * 80)
    print(f"Retrieved {len(chunks)} chunks")
    print("=" * 80)

    for index, chunk in enumerate(chunks, start=1):

        print()

        print(f"Chunk {index}")

        print("-" * 80)

        print(f"Chunk ID    : {chunk.chunk_id}")
        print(f"Company     : {chunk.company}")
        print(f"Report Year : {chunk.report_year}")

        print()

        print(chunk.text[:700])

        print()


if __name__ == "__main__":
    main()