from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from config import CHAT_MODEL_NAME, CHAT_MODEL_KWARGS

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY_CHAT")

model_name = CHAT_MODEL_NAME
model_kwargs = CHAT_MODEL_KWARGS

def respond_to_query(query):
    
    llm = ChatOpenAI(
        api_key=api_key,
        model=model_name,
        **model_kwargs
    )
    response = llm.invoke(query)
    # print("=" * 50)
    # print(f"Query: {query}")
    print("-" * 50)
    print(f"Response: {response.content}")
    
    return response