import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.ingestion.chunker import chunk_text_data
from src.ingestion.embedder import generate_embeddings
from src.ingestion.loader import load_pdf_files
from config import EMBEDDING_BATCH_SIZE


def main():
    # Load PDF files
    raw_data = load_pdf_files()
    # Chunk text data
    chunked_data = chunk_text_data(raw_data)
    # Generate embeddings
    embeddings = generate_embeddings(chunked_data, batch_size=EMBEDDING_BATCH_SIZE)


if __name__ == "__main__":
    main()
