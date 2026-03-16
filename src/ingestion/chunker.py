from langchain_text_splitters import CharacterTextSplitter

def chunk_text_data(data):
    print("Chunking text data...")
    text_splitter = CharacterTextSplitter(
        chunk_size=500, 
        chunk_overlap=50, 
        separator = '. '
    )

    texts = []

    for doc in data:
        chunks = text_splitter.split_documents(doc)
        text = []
        for i, chunk in enumerate(chunks):
            chunk.metadata["chunk_idx"] = i
            text.append(chunk)
        texts.append(text)
            
    print(f"Created pdf files: {len(texts)}")
    print(f"Created average chunks per file: {sum(len(chunk) for chunk in texts) / len(texts) if texts else 0}")

    return texts
