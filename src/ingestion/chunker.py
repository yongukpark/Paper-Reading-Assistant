from langchain_text_splitters import CharacterTextSplitter   

def chunk_text_data(data):
    print("Chunking text data...")
    text_splitter = CharacterTextSplitter(
        chunk_size=500, 
        chunk_overlap=50, 
        separator = '. '
    )

    texts = [text_splitter.split_documents(text) for text in data]
    print(f"Created pdf files: {len(texts)}")
    print(f"Created average chunks per file: {sum(len(chunk) for chunk in texts) / len(texts) if texts else 0}")

    return texts