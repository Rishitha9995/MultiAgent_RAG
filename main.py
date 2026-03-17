# main.py

import os
import time

from preprocessing.dataset_loader import load_documents
from preprocessing.chunking import chunk_documents
from embeddings.embedder import get_embedding_model
from vector_db.build_vector_db import build_vector_store
from textblob import TextBlob

# -----------------------------
# IMPORT AGENTS
# -----------------------------
from agents.query_agent import autocorrect_query
from agents.router_agent import choose_dataset
from agents.retriever_agent import retrieve_documents
from agents.reasoning_agent import generate_response
from agents.formatter_agent import format_points
from agents.explainability_agent import explainability_agent
from agents.evaluate_rag_agent import evaluate_rag


# -----------------------------
# SYSTEM START
# -----------------------------
print("\n===== Multi-Agent RAG System Initialized =====")
print("Agents: Query | Router | Retriever | Reasoning | Formatter | Evaluation\n")

print("Initializing system...\n")

embedding_model = get_embedding_model()


# -----------------------------
# LOAD VECTOR DATABASE
# -----------------------------
if os.path.exists("vector_db/legal_index") and os.path.exists("vector_db/business_index"):

    print("Loading existing vector databases...")

    legal_db = build_vector_store([], embedding_model, "vector_db/legal_index")
    business_db = build_vector_store([], embedding_model, "vector_db/business_index")

else:

    print("Building vector databases for first time...\n")

    legal_docs = load_documents("data/legal_cases")
    business_docs = load_documents("data/business_docs")

    legal_chunks = chunk_documents(legal_docs)
    business_chunks = chunk_documents(business_docs)

    legal_db = build_vector_store(
        legal_chunks,
        embedding_model,
        "vector_db/legal_index"
    )

    business_db = build_vector_store(
        business_chunks,
        embedding_model,
        "vector_db/business_index"
    )

print("\nSystem Ready!\n")


# -----------------------------
# QUERY LOOP
# -----------------------------
while True:

    query = input("\nEnter your question (or type exit): ")

    if query.lower() == "exit":
        print("\nExiting system...")
        break

    start = time.time()

    # -----------------------------
    # Query Agent
    # -----------------------------
    print("\n[Query Agent] Checking and correcting query...")
    query = autocorrect_query(query)

    # -----------------------------
    # Router Agent
    # -----------------------------
    print("[Router Agent] Determining appropriate dataset...")
    dataset = choose_dataset(query)

    print("[Router Agent] Dataset Selected:", dataset)

    # -----------------------------
    # Retriever Agent
    # -----------------------------
    print("[Retriever Agent] Retrieving top relevant documents...")

    if dataset == "business":
        docs, results = retrieve_documents(query, business_db, dataset)
    else:
        docs, results = retrieve_documents(query, legal_db, dataset)

    docs = [doc for doc, score in results]

    # -----------------------------
    # Reasoning Agent
    # -----------------------------
    print("[Reasoning Agent] Generating answer from retrieved context...")
    answer = generate_response(query, docs)

    # -----------------------------
    # Formatter Agent
    # -----------------------------
    print("[Formatter Agent] Formatting response into bullet points...")
    answer = format_points(answer)

    end = time.time()

    # -----------------------------
    # FINAL ANSWER
    # -----------------------------
    print("\nFinal Answer:\n")
    print(answer)

    # -----------------------------
    # Explainability Agent
    # -----------------------------
    print("\n[Explainability Agent] Explaining retrieved documents...")

    explanations = explainability_agent(results)

    print("\nTop Retrieved Documents:\n")

    for e in explanations:

        print(f"{e['rank']}. {e['source']}")
        print(f"   similarity_score: {e['score']}")
        print(f"   reason: {e['reason']}")
        print()

    # -----------------------------
    # Evaluation Agent
    # -----------------------------
    print("[Evaluation Agent] Computing RAG metrics...")
    evaluate_rag(query, answer, docs, embedding_model)

    print("\nResponse Time:", round(end-start,2), "seconds")