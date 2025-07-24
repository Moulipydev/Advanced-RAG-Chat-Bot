from langchain.chains import RetrievalQA
from langchain_mistralai.chat_models import ChatMistralAI

# Load Mistral API key from .env
api_key = "pw44cu6BFRLOBCOqt3rPS9ZEm3CUeTEQ"

# Setup Mistral Client + LLM
mistral_llm = ChatMistralAI(
    api_key=api_key,
    model="mistral-large-latest",
    temperature=0.3
)

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate

# Load embedding model (same one used during indexing)
embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en")

# Load vectorstore from disk
vectorstore = Chroma(persist_directory="./db", embedding_function=embedding_model)

# Create Retriever
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})


prompt_template = """
You are an intelligent assistant helping users answer questions based on documents.

Only use the context provided below to answer. If the answer is not in the context, say "I don't know".

Context:
{DOB}

Question:
{can you provide a DOB of the context?}
"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template,
)

# RAG Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=mistral_llm,
    retriever=retriever,
    #chain_type_kwargs={"prompt": prompt},
    return_source_documents=True
)

# Ask a question
while True:
    query = input("🧠 Ask something about your PDFs:\n> ")
    if query.lower() == "x":
        break
    result = qa_chain({"query": query})

    # Output response
    print("\n💬 Answer:\n", result["result"])

# # Optional: Show sources
# # print("\n📚 Sources:")
# for doc in result["source_documents"]:
#     print("-", doc.metadata.get("source", "Unknown PDF"))
