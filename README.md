🤖 Advanced RAG Chat BotAn end-to-end Retrieval-Augmented Generation (RAG) system designed to perform intelligent, context-aware document Question-Answering (QA) with accurate source attribution and low latency.

🌟 Key Features
Advanced Retrieval Strategies: Utilizes hybrid search (Dense Embeddings + Sparse Keyword Search / BM25) and re-ranking to maximize contextual precision.

Intelligent Document Chunking: Implements semantic/recursive chunking to maintain context boundaries across multi-page documents (PDFs, Markdown, Text).

Source Attribution & Citations: Returns accurate references and citations alongside generated responses to prevent hallucinations.

Scalable Vector Database: Integrated with vector search for fast similarity queries and scalable data storage.

Interactive UI: Built-in web interface for seamless document upload, querying, and chat history management.

🏗️ System Architecture

Ingestion & Chunking: Raw documents are loaded, cleaned, and split into semantic chunks.

Embedding & Indexing: Chunks are embedded using high-dimensional vector models and indexed into a Vector Database.

Retrieval & Re-ranking: User queries trigger semantic retrieval, followed by a re-ranking pipeline to prioritize top-$K$ relevant context blocks.

Contextual Generation: Retrieved context is combined with the user query into a structured prompt and passed to the LLM for response synthesis.

🚀 Getting Started

Prerequisites
Python: 3.9 or higher
API Keys: OpenAI / Anthropic / HuggingFace API keys (as required by your setup)

1. Clone the RepositoryBashgit clone https://github.com/Moulipydev/Advanced-RAG-Chat-Bot.git
cd Advanced-RAG-Chat-Bot
2. Set Up Virtual Environment & DependenciesBashpython -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Environment VariablesCreate a .env file in the root directory:Code snippetOPENAI_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_vector_db_key_here  # Optional depending on your vector DB
4. Run the ApplicationBashpython app.py

🛠️ Tech Stack
Language: PythonLLM 
Orchestration: LangChain / LlamaIndex
Embeddings & LLM: OpenAI / HuggingFace
Vector Storage: FAISS / Pinecone / ChromaDB / Qdrant
