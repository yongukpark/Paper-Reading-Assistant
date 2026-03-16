from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
VECTORSTORE_PERSIST_DIRECTORY = str(DATA_DIR / "paper_context_embeddings")

EMBEDDING_MODEL_NAME = "Qwen/Qwen3-Embedding-0.6B"
EMBEDDING_MODEL_KWARGS = {"device": "mps", "trust_remote_code": True}
EMBEDDING_ENCODE_KWARGS = {"normalize_embeddings": True}
EMBEDDING_BATCH_SIZE = 2

CHAT_MODEL_NAME = "gpt-4o-mini"
CHAT_MODEL_KWARGS = {"temperature": 0, "max_tokens": 200}
