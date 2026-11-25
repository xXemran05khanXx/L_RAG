from app.llms import get_llms

def generate_answer(llms,query,documents):

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

    for model_name, llm in llms:
        try:
            print(f"\nTrying model: {model_name}")
            response = llm.invoke(prompt)
            print(f"Successfully answered using: {model_name}")
            return response.content
        
        except Exception as e:
            error_message = str(e).lower()
            temporary_errors = [
                "503",
                "unavailable",
                "429",
                "resource_exhausted",
                "404",
                "not_found"
            ]

            if any(error in error_message for error in temporary_errors):
                print(f"Model {model_name} failed: {e}")
                print("Trying next fallback model........")

                continue

            raise
        raise RuntimeError(
            "All Gemini models failed. Please try again later."
        )