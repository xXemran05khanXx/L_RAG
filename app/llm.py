from langchain_google_genai import ChatGoogleGenerativeAI   

def get_llm():

    llm=ChatGoogleGenerativeAI (
        model="gemini-3.8-flash",
        temperature=0
    )

    return llm