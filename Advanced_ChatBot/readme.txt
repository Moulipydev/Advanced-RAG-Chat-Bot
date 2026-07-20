

Requirements: 

langchain ✅
langchain-community ✅
langchainhub ✅
langchain-core ✅
chromadb ✅
python-dotenv ✅
transformers ✅
sentence-transformers ✅
PyPDF2 ✅


rag-mistral-chatbot/
│
├── main.py                   # Entry point
├── .env                      # Store your Mistral API key securely
│
├── /data/                    # Place your PDFs here
│   └── sample.pdf
│
├── /db/                      # Chroma vectorstore files (auto-generated)
│
├── requirements.txt
