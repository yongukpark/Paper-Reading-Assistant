from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from tqdm import tqdm
from dotenv import load_dotenv
import torch
import os
from config import EMBEDDING_MODEL_NAME, EMBEDDING_ENCODE_KWARGS, EMBEDDING_MODEL_KWARGS, VECTORSTORE_PERSIST_DIRECTORY

load_dotenv()

def generate_embeddings(new_documents, batch_size=2): # 배치 사이즈 조절 가능
    print("Initializing Embedding Model...")
    embeddings_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        encode_kwargs=EMBEDDING_ENCODE_KWARGS,
        model_kwargs=EMBEDDING_MODEL_KWARGS
    )
    
    # tqdm으로 진행 상황 표시
    print(f"Generating embeddings for {len(new_documents)} documents...")

    if batch_size < 1:
        raise ValueError("batch_size must be greater than 0")

    if os.path.exists(VECTORSTORE_PERSIST_DIRECTORY):
        print("Loading existing embeddings...")
        vectorstore = Chroma(
            collection_name="paper_collection",
            embedding_function=embeddings_model,
            persist_directory=VECTORSTORE_PERSIST_DIRECTORY
        )
        for i in tqdm(range(0, len(new_documents), batch_size), desc="number of documents processed"):
            batch_documents = [
                document
                for document_group in new_documents[i:i + batch_size]
                for document in document_group
            ]
            vectorstore.add_documents(batch_documents)
            print(f'{min(i + batch_size, len(new_documents))} 번 : {vectorstore._collection.count()}')
            torch.mps.empty_cache()
    else:
        vectorstore = Chroma.from_documents(
                documents=[
                    document
                    for document_group in new_documents[:batch_size]
                    for document in document_group
                ],
                embedding=embeddings_model,
                collection_name=f"paper_collection",
                persist_directory=VECTORSTORE_PERSIST_DIRECTORY
            )
        for i in tqdm(range(batch_size, len(new_documents), batch_size), desc="number of documents processed"):
            batch_documents = [
                document
                for document_group in new_documents[i:i + batch_size]
                for document in document_group
            ]
            vectorstore.add_documents(batch_documents)
            print(f'{min(i + batch_size, len(new_documents))} 번 : {vectorstore._collection.count()}')
            torch.mps.empty_cache()
