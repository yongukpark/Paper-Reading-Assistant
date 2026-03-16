import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.chat.chat import respond_to_query
from src.retrieval.retriever import load_vectorstore


def main():
    query = "Exclusive Self Attention가 해결하고자하는 문제는 뭐야?"

    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    contexts = retriever.invoke(query)

    # ====어떤 context들이 retrieval 되었는지 확인하기 위해 출력====
    # for i, context in enumerate(contexts):
    #     print("-" * 50)
    #     print(f"Context {i+1}: {context.metadata} : {context.page_content[:200]}...")  # Print the first 200 characters of each context

    context = "\n\n".join(context.page_content for context in contexts)
    
    print("=" * 50, "Naive", "=" * 50)
    respond_to_query(query)
    print("=" * 50, "RAG", "=" * 50)
    respond_to_query(query, context)


if __name__ == "__main__":
    main()