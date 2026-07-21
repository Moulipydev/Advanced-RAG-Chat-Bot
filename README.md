🚀 Agentic AI Assistant with LangChain, Mistral, RAG & Memory

An intelligent Agentic AI Assistant built using LangChain, Mistral AI, RAG (Retrieval-Augmented Generation), ChromaDB, and Conversational Memory.

This project demonstrates how modern AI agents can reason, use multiple tools, retrieve information from private knowledge bases, search the web for real-time information, and maintain conversational context across interactions.

Unlike a traditional chatbot, this agent can dynamically decide which tool to use based on the user's query.

✨ Features
🧠 Conversational AI powered by Mistral AI
📄 RAG-based document question answering using PDF files
🔍 Real-time web search using Tavily Search
💾 Persistent conversational memory
🛠 Tool-using AI Agent built with LangChain
📚 Local vector database using ChromaDB
🔎 Semantic search using HuggingFace Embeddings
💬 Multi-turn conversation support
⚡ Modular architecture for adding new tools
🖥 CLI-based interactive chatbot
🏗 Architecture
                User
                  │
                  ▼
          LangChain Agent
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
   Tavily Search        RAG Tool
                            │
                            ▼
                     Chroma Vector DB
                            │
                            ▼
                  HuggingFace Embeddings
                            │
                            ▼
                          PDFs

                  ▲
                  │
           Conversation Memory

                  ▲
                  │
             Mistral AI API
🛠 Tech Stack
AI & LLM
LangChain
Mistral AI
HuggingFace Embeddings
Retrieval
ChromaDB
RecursiveCharacterTextSplitter
PyPDFLoader
Search
Tavily Search API
Memory
ConversationBufferMemory
FileChatMessageHistory
Programming Language
Python 3.12
📂 Project Structure
langchain-agent-tools/

│
├── data/
│      sample.pdf
│
├── vectorstore/
│
├── chat_history.json
│
├── .env
│
├── agent_with_tools.py
│
├── requirements.txt
│
└── README.md
⚙ Workflow
1. Load PDFs

The application loads PDF documents using PyPDFLoader.

↓

2. Split Documents

Documents are split into semantic chunks using RecursiveCharacterTextSplitter.

↓

3. Generate Embeddings

Each chunk is converted into vector embeddings using HuggingFace.

↓

4. Store in ChromaDB

Embeddings are stored inside a local Chroma Vector Database.

↓

5. User Query

The user asks a question.

↓

6. Agent Reasoning

The LangChain Agent decides whether it should

Search the Web
Query the PDF Knowledge Base

↓

7. Tool Execution

The selected tool executes.

↓

8. Final Response

The result is combined with conversational memory and returned to the user.

📌 Example Queries
🌐 General Knowledge
Who won the 2024 ICC Men's T20 World Cup?

↓

Agent selects Tavily Search

📄 PDF Questions
What is this PDF about?

↓

Agent selects RAG Tool

💬 Follow-up Conversation
Who won the T20 World Cup?

↓

Who was the captain?

↓

Where was the final played?

The agent remembers previous conversation context using Conversation Memory.

🚀 Future Enhancements
LangGraph integration
LangSmith tracing & evaluation
Multi-Agent workflows
Custom business automation tools
FastAPI REST API
Streamlit / React frontend
Persistent memory using PostgreSQL or Redis
Docker containerization
Cloud deployment (AWS)
🎯 Learning Outcomes

This project helped me gain hands-on experience with:

Agentic AI concepts
LangChain Agents
Tool Calling
Retrieval-Augmented Generation (RAG)
Vector Databases
Embeddings
Conversational Memory
Prompt Engineering
LLM Integration
Semantic Search
Multi-tool AI Systems
📷 Demo
User:
Who won the 2024 T20 World Cup?

Agent:
India won the 2024 ICC Men's T20 World Cup.

User:
Who was the captain?

Agent:
Rohit Sharma was the captain of the Indian team.
⭐ Why This Project?

Traditional chatbots simply generate responses.

This project demonstrates an Agentic AI System capable of:

Reasoning before answering
Selecting the appropriate tool autonomously
Retrieving information from private documents
Searching the web for current information
Maintaining conversational memory
Delivering context-aware responses

This architecture closely resembles the design patterns used in modern AI applications and enterprise GenAI systems.
