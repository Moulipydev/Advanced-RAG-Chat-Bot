Mistral:
API_KEY = pw44cu6BFRLOBCOqt3rPS9ZEm3CUeTEQ

Tavily: (Search Engine)
API_KEY = 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

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