from langchain_google_genai import ChatGoogleGenerativeAI   

def get_llms():
    models = [
        "gemini-3.5-flash-lite",
        "gemini-3.1-flash-lite",
        "gemini-3.8-flash",
        "gemini-4-hydrogen",
        "gemini-3.6-flash"
    ]

    llms = []

    for model_name in models:
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            timeout=60,
            max_retries=0,
            temperature=0
        )

        llms.append((model_name, llm))

    return llms