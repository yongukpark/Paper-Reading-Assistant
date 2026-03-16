from langchain_chroma import Chroma

from config import VECTORSTORE_PERSIST_DIRECTORY
from src.embedding_model import build_embeddings

def load_vectorstore():
    embeddings_model = build_embeddings()
    
    vectorstore = Chroma(
        collection_name="paper_collection",
        embedding_function=embeddings_model,
        persist_directory=VECTORSTORE_PERSIST_DIRECTORY
    )
    
    return vectorstore
