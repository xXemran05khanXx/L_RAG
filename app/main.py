from dotenv import load_dotenv
load_dotenv()

from app.document_loader import load_and_split_docs
from app.vector_store import create_vector_store
from app.retriever import retriver_documents
from app.rag_chain import generate_answer
from app.llm import get_llm
from app.performance_tracker import PerformanceTracker

def main():

    tracker = PerformanceTracker()

    print("\n========== RAG APPLICATION ==========")

 # Step 1: Document Loading
    tracker.start("Document Loading")

    chunks = load_and_split_docs("data/company_policy.txt")

    tracker.end()
    print(f"Total chunks: {len(chunks)}")

    # Step 2: Vector Store Creation
    tracker.start("Vector Store Creation")

    vector_store, embeddings = create_vector_store(chunks)

    tracker.end()

    # Step 3: Load Gemini
    tracker.start("Gemini Initialization")

    llm = get_llm()

    tracker.end()

    # Step 4: Similarity Search
    query = "What is policy title?"

    tracker.start("Similarity Search")

    result = retriver_documents(vector_store, query)

    tracker.end()
    print(f"Retrieved documents: {len(result)}")

    # Step 5: Generate Answer
    tracker.start("Gemini Answer Generation")

    answer = generate_answer(llm, query, result)

    tracker.end()

    print("\n========== FINAL ANSWER ==========")
    print(answer)

    # Step 6: Performance Report
    tracker.report()


if __name__ == "__main__":
    main()
