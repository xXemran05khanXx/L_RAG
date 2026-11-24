from dotenv import load_dotenv
load_dotenv()

from app.document_loader import load_and_split_docs
from app.vector_store import create_vector_store
from app.retriever import retriver_documents

def main():
    print("--------Loading documents:--------")

    chunks = load_and_split_docs("data/company_policy.txt")
    print(f"Total chunks: {len(chunks)}")

    print("\n--------Creating Vector Store:--------")

    vector_store, embeddings= create_vector_store(chunks)
   
    print("Vector Store created successfully!")

    print("--------Similarity search--------")
    query="ELIGIBILITY"
    result= retriver_documents(vector_store, query)

    print("\nUser Question:", query)
    print("\nRetrieved Document:")

    for i, doc in enumerate(result,start=1):
        print(f"\n--------Result {i}--------")
        print(doc.page_content)
    

if __name__ == "__main__":
    main()