import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser    

from config import CHAT_MODEL_NAME, CHAT_MODEL_KWARGS

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY_CHAT")

model_name = CHAT_MODEL_NAME
model_kwargs = CHAT_MODEL_KWARGS

def respond_to_query(query, context:str = ""):
    messages = [
        ("system", "너는 논문에 대해 질문을 받고 답변을 해주는 역할이다. 다음 context를 바탕으로 질문에 답변해라."),
        ("user", "{context}\n\n질문: {query}"),
    ]
    
    prompt = ChatPromptTemplate.from_messages(messages)
    
    llm = ChatOpenAI(
        api_key=api_key,
        model=model_name,
        **model_kwargs
    )
    
    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser
    
    response_text = []
    for chunk in chain.stream({"context": context, "query": query}):
        print(chunk, end="", flush=True)
        response_text.append(chunk)
    print('\n')
    
    response_text = "".join(response_text)
    
    return response_text