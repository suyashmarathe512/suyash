# LLM-Powered Booking Analytics & QA System

This project demonstrates an LLM-powered system for analyzing hotel booking data and answering user queries using a Retrieval Augmented Generation (RAG) approach. It leverages FastAPI for building the API, Sentence Transformers for embeddings, and ChromaDB for efficient vector search.

## Features

- **Data Preprocessing:** Loads, cleans, and prepares hotel booking data from a CSV file.
- **Analytics & Reporting:** Computes key metrics like revenue trends, cancellation rate, lead time statistics, geographical distribution, and more.
- **Retrieval-Augmented QA System:** Allows users to ask natural language questions about the booking data. The system retrieves relevant context from the data and uses an LLM (simulated in this case) to generate answers.
- **FastAPI Integration:** Exposes analytics and QA functionality through a RESTful API.
- **ChromaDB for Vector Search:** Uses ChromaDB for efficient storage and retrieval of booking record embeddings.
- **Sentence Transformers for Embeddings:** Utilizes Sentence Transformers to generate semantic embeddings for booking records.

## Setup and Usage

1. **Clone the Repository:**
