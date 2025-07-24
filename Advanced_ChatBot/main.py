import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load env vars
load_dotenv()
pdf_dir = "data"

def load_documents():
    all_docs = []
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_dir, file))
            docs = loader.load()
            all_docs.extend(docs)
    return all_docs

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)

# Load & chunk
raw_docs = load_documents()
print(f"✅ Loaded {len(raw_docs)} raw pages.")

chunked_docs = chunk_documents(raw_docs)
print(f"✅ Chunked into {len(chunked_docs)} chunks.")

#=============================================================================
# Save embeddings to vectorstore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Setup embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create or load vectorstore
vectorstore = Chroma.from_documents(
    documents=chunked_docs,
    embedding=embedding_model,
    persist_directory="./db"
)

vectorstore.persist()
print("✅ Vectorstore created and saved.")
