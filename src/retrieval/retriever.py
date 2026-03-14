from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL_NAME, EMBEDDING_ENCODE_KWARGS, EMBEDDING_MODEL_KWARGS, VECTORSTORE_PERSIST_DIRECTORY

def load_vectorstore():
    embeddings_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        encode_kwargs=EMBEDDING_ENCODE_KWARGS,
        model_kwargs=EMBEDDING_MODEL_KWARGS
        )
    
    vectorstore = Chroma(
        collection_name="paper_collection",
        embedding_function=embeddings_model,
        persist_directory=VECTORSTORE_PERSIST_DIRECTORY
    )
    
    return vectorstore
