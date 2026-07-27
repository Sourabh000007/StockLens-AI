from app.rag.hybrid_retrieval_service import HybridRetrievalService


def main():

    service = HybridRetrievalService()

    chunks = service.retrieve(
        question="What are TCS AI initiatives?",
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
        print(f"Chunk ID : {chunk.chunk_id}")
        print(f"Distance : {chunk.distance:.4f}")
        print()
        print(chunk.text[:600])


if __name__ == "__main__":
    main()