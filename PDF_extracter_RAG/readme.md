# PDF_extracter_RAG 🧾🔍

A Retrieval-Augmented Generation (RAG) toolkit for extracting, querying, and summarizing data from PDF documents.

---

## 🧩 Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Architecture](#architecture)  
- [Setup & Installation](#setup--installation)  
- [Usage](#usage)  
  - [Basic Extraction](#basic-extraction)  
  - [Uploading & Indexing](#uploading--indexing)  
  - [Query Chat Interface](#query-chat-interface)  
- [Configuration](#configuration)  
- [Examples](#examples)  
- [Contributing](#contributing)  
- [License](#license)  
- [Acknowledgements & References](#acknowledgements--references)

---

## 📝 Overview

This tool helps you:

- Parse text (and possibly layout structures like tables/headings) from PDFs  
- Create vector embeddings & store in a lightweight retrieval index  
- Chat with your documents using LLM-powered RAG queries  
- Support for summarization, Q&A, and document analysis

---

## ✅ Features

- PDF ingestion with [pdfminer / PyPDF2 / Camelot – adapt as used]  
- Embedding generation using [sentence-transformers / OpenAI embeddings]  
- Simple vector store backend (e.g. FAISS, Chroma)  
- Prompt-engineered chat interface powered by OpenAI / Hugging Face LLMs  
- Optional: layout-aware processing (tables, headings, footnotes)  
- CLI and library modes for flexibility in automation

---

## 🛠️ Architecture

1. **PDF Processor** – Extracts text and metadata  
2. **Embedder** – Converts text chunks → embedding vectors  
3. **Indexer** – Stores vectors, supports semantic similarity search  
4. **Query Agent** – Fetches relevant context and prompts an LLM  
5. **Chat Module** – Conversational loop with memory and follow‑ups

---

## ⚙️ Setup & Installation

```bash
git clone https://github.com/suyashmarathe512/suyash.git
cd suyash/PDF_extracter_RAG

# Create and activate venv
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
