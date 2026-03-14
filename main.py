from src.retrieval.retriever import load_vectorstore
from src.chat.chat import respond_to_query
     
def main():
    query = "Exclusive Self Attentio가 해결하고자하는 문제는 뭐야?"
    
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    contexts = retriever.invoke(query)
    
    for i, context in enumerate(contexts):
        print("-" * 50)
        print(f"Context {i+1}: {context.metadata} : {context.page_content[:200]}...")  # Print the first 200 characters of each context
    
    context = "\n\n".join(context.page_content for context in contexts)
    
    rag_query = f"""
        너는 논문에 대해 질문을 받고 답변을 해주는 역할이다. 다음 context를 바탕으로 질문에 답변해라.
        {context}
        질문: {query}
        답변 : """
    
    print("=" * 50, "Naive", "=" * 50)
    respond_to_query(query)
    print("=" * 50, "RAG", "=" * 50)
    respond_to_query(rag_query)

if __name__ == "__main__":
    main()