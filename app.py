from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import os

# -----------------------------
# Load LLM
# -----------------------------
llm = ChatOpenAI(model="gpt-4o-mini")

# -----------------------------
# Load PDF
# -----------------------------
pdf_path = "documents/sample.pdf"

loader = PyPDFLoader(pdf_path)
documents = loader.load()

# -----------------------------
# Split text into chunks
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)

docs = text_splitter.split_documents(documents)

# -----------------------------
# Create embeddings
# -----------------------------
embeddings = OpenAIEmbeddings()

# -----------------------------
# Store in vector database
# -----------------------------
db = Chroma.from_documents(docs, embeddings)

retriever = db.as_retriever()

# -----------------------------
# Create RAG pipeline
# -----------------------------
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

# -----------------------------
# Chat loop
# -----------------------------
print("\nPDF RAG Chatbot Ready (type 'exit' to quit)\n")

while True:
    query = input("Ask question: ")

    if query.lower() == "exit":
        break

    response = qa.run(query)
    print("\nAnswer:", response, "\n")

