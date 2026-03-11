from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from tqdm import tqdm
from dotenv import load_dotenv
import torch

load_dotenv()

model_kwargs = {'device': 'mps', 'trust_remote_code': True}      
encode_kwargs = {'normalize_embeddings': True} 

def generate_embeddings(documents, batch_size=2): # 배치 사이즈 조절 가능
    print("Initializing Embedding Model...")
    embeddings_model = HuggingFaceEmbeddings(
        model_name="Qwen/Qwen3-Embedding-0.6B",
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    # tqdm으로 진행 상황 표시
    print(f"Generating embeddings for {len(documents)} documents...")

    for i in tqdm(range(0, len(documents)), desc="number of documents processed"):
        vectorstore = Chroma.from_documents(
            documents=documents[i],
            embedding=embeddings_model,
            collection_name=f"paper_collection",
            persist_directory="./data/embeddings"
        )
        torch.mps.empty_cache()