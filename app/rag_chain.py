from app.llm import get_llm

def generate_answer(llm,query,documents):

    context = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = f"""
     You are a helpful company policy assistant.

    Answer the question using ONLY the context below.

    If the answer is not available in the context,
    say "Answer not found in company policy."

    Context:
    {context}

    Question:
    {query}

    Answer:
    
    """

    response = llm.invoke(prompt)
    return response.content