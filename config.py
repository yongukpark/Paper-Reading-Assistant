EMBEDDING_MODEL_NAME = "Qwen/Qwen3-Embedding-0.6B"
EMBEDDING_MODEL_KWARGS = {'device': 'mps', 'trust_remote_code': True}      
EMBEDDING_ENCODE_KWARGS = {'normalize_embeddings': True} 
EMBEDDING_BATCH_SIZE = 2

VECTORSTORE_PERSIST_DIRECTORY = "./data/paper_context_embeddings"

CHAT_MODEL_NAME = "gpt-4o-mini"
CHAT_MODEL_KWARGS = {'temperature': 0, 'max_tokens': 200}