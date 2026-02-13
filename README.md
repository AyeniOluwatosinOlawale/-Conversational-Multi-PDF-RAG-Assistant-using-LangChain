# -Conversational-Multi-PDF-RAG-Assistant-using-LangChain
This project implements a Retrieval Augmented Generation (RAG) system that allows users to interact conversationally with multiple PDF documents stored locally. The assistant retrieves relevant knowledge from PDFs and generates context-aware responses using Large Language Models (LLMs).
This solution mimics real-world enterprise knowledge assistants used in finance, healthcare, research, and legal domains.

🚀 Project Overview

Traditional LLMs rely only on training data and may hallucinate or lack access to private knowledge. This project solves that limitation by combining:

Semantic document retrieval

Conversational memory

Multi-PDF knowledge integration

Persistent vector database storage

The assistant enables users to ask questions naturally and receive answers grounded in uploaded documents.
🏗 System Architecture
Local PDF Documents
        ↓
Document Loader
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
Vector Database (Chroma)
        ↓
Retriever
        ↓
Conversational Memory
        ↓
LLM Response Generator

✨ Features
✅ Multi-PDF Knowledge Base

Automatically loads all PDFs from a local directory.

Supports scaling with multiple research or enterprise documents.

✅ Conversational Chat Memory

Maintains context across multiple questions.

Provides ChatGPT-like interaction experience.

✅ Persistent Vector Storage

Embeddings stored locally.

Eliminates need for rebuilding knowledge base on each run.

✅ Semantic Document Retrieval

Retrieves most relevant document chunks using embeddings.

Reduces hallucination and improves response accuracy.

✅ Modular and Scalable Design

Easy to extend with UI, agents, or additional data sources.

🛠 Technologies Used

Python

LangChain

OpenAI LLMs

Chroma Vector Database

PyPDF Loader

Recursive Text Chunking

Conversational Retrieval Chain

📂 Project Structure
pdf_chatbot/
│
├── app.py
├── documents/
│     ├── file1.pdf
│     ├── file2.pdf
│     └── ...
│
└── vector_db/
