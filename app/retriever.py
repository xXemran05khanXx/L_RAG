def retriver_documents(vector_store, query):
    result = vector_store.similarity_search(
        query,
        k=1
    )

    return result