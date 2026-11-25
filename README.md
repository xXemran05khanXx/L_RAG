# Gemini-Powered RAG Application

A Retrieval-Augmented Generation (RAG) application built using Python, LangChain, Google Gemini, and FAISS.

This application loads company policy documents, splits them into smaller chunks, generates vector embeddings, stores them in a FAISS vector database, retrieves relevant information based on user questions, and generates answers using Google Gemini.

## Features

- Document loading from text files
- Text splitting and chunking
- Google Gemini embeddings
- FAISS vector database
- Semantic similarity search
- Gemini-powered answer generation
- Model fallback support
- Performance tracking
- Interactive question-answering

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| LangChain | RAG pipeline |
| Google Gemini | Embeddings and LLM |
| FAISS | Vector database |
| python-dotenv | Environment variables |


## Project Structure

```text
L_RAG/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   ├── rag_chain.py
│   └── performance_tracker.py
│
├── data/
│   └── company_policy.txt
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md