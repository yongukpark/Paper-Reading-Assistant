from langchain_huggingface import HuggingFaceEmbeddings

from config import EMBEDDING_ENCODE_KWARGS, EMBEDDING_MODEL_KWARGS, EMBEDDING_MODEL_NAME


def build_embeddings() -> HuggingFaceEmbeddings:
    try:
        return HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
            encode_kwargs=EMBEDDING_ENCODE_KWARGS,
            model_kwargs=EMBEDDING_MODEL_KWARGS,
        )
    except ValueError as exc:
        message = str(exc)
        if "model type `qwen3`" in message or "KeyError: 'qwen3'" in message:
            raise RuntimeError(
                "Failed to load Qwen3 embedding model. "
                "Check that the active environment has a recent `transformers` build "
                "and reinstall the dependency if needed. "
                "Recommended: `pip install -U transformers sentence-transformers`."
            ) from exc
        raise
