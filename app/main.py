from dotenv import load_dotenv

load_dotenv()

from app.document_loader import load_and_split_docs
from app.vector_store import create_vector_store

def main():
    print("Loading documents:")

    chunks = load_and_split_docs("data/company_policy.txt")
    print(f"Total chunks: {len(chunks)}")

    print("\nCreating Vector Store:")

    vector_store, embed= create_vector_store(chunks)
   
    print("Vector Store created successfully!")
    print(embed)

if __name__ == "__main__":
    main()