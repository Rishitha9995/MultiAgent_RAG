# 📊 Multi-Agent RAG Framework for Business Intelligence

## 🚀 Overview

This project presents a Multi-Agent Retrieval-Augmented Generation (RAG) system that integrates business and legal datasets to generate accurate, context-aware, and explainable insights.
It enhances traditional RAG by incorporating metadata-aware retrieval and multi-agent intelligence.

---

## ❗ Problem Statement

* Business & legal data is fragmented across multiple sources
* Traditional RAG systems lack domain awareness, metadata usage, and explainability
* LLMs may generate generic or unverified responses
* Lack of structured, actionable outputs

---

## 💡 Proposed Solution

A metadata-driven multi-agent RAG system that improves:

* Query understanding
* Context-aware retrieval
* Metadata-based filtering
* Source-grounded response generation
* Structured and explainable outputs

---

## 🧠 Multi-Agent Architecture

* Query Agent → Understands & refines query
* Router Agent → Selects Business / Legal dataset using metadata
* Retriever Agent → Fetches Top-K documents using similarity + metadata filtering
* Reasoning Agent → Generates answer using FLAN-T5
* Formatter Agent → Produces structured output

---

## 🏷️ Metadata Integration (Key Feature)

Metadata is attached to each document during preprocessing and used throughout the pipeline:

* Metadata Fields:

  * Domain (Business / Legal)
  * Source (dataset origin)
  * Document type
  * Chunk information

* Why Metadata Matters:

  * Enables domain-specific retrieval
  * Improves search accuracy
  * Helps router agent decision-making
  * Adds context to final responses

---

## 🔍 Explainability

* Displays Top-K retrieved documents
* Shows similarity scores
* Includes metadata (source, domain, type)
* Provides reasoning for document selection

Ensures transparency, traceability, and trust

---

## 📂 Data & Processing

* Datasets:

  * Business: Alpaca Cleaned
  * Legal: LEDGAR (LexGLUE)

* Preprocessing:

  * Text cleaning & chunking
  * Metadata tagging (domain, source, type, chunk details)

* Embeddings:

  * Sentence Transformers (all-MiniLM-L6-v2)
  * Stored in FAISS vector database

---

## ⚙️ Retrieval Technique

* Semantic Search (Top-K similarity)
* Hybrid retrieval using similarity and metadata filtering

---

## 📈 Evaluation Metrics

* Relevance Score → Query-document alignment
* Confidence Score → Response reliability
* Answer Quality → Correctness and completeness
* Retrieval Accuracy → Effectiveness of retrieval

---

## 🖥️ Tech Stack

* Backend: FastAPI
* Frontend: React.js
* Vector DB: FAISS
* LLM: FLAN-T5
* Embeddings: Sentence Transformers

---

## ✅ Results

* Generated accurate, context-aware responses
* Provided source and metadata-backed answers
* Improved retrieval precision using metadata filtering
* Built a web-based interactive system

---

## 🔮 Future Scope

* Advanced metadata-based ranking
* Dynamic metadata enrichment
* Improved agent-level decision-making
* Scalable multi-domain support

---

## 🎯 Conclusion

This project shows that combining multi-agent architecture, metadata-aware retrieval, and explainability improves the accuracy, transparency, and usability of RAG systems for business intelligence.


