import os
from glob import glob

from langchain_community.document_loaders import PyPDFLoader   
# ====document loading====
def load_pdf_files():
    print("Loading PDF files from data directory...")

    pdf_files = glob(os.path.join("data/raw", "*.pdf"))
    print(pdf_files)

    data = []
    for pdf_file in pdf_files:
        data.append(list(PyPDFLoader(pdf_file).load()))

    print(data[0][0].metadata)
    return data