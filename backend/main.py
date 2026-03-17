#main.py
import os
import time

from preprocessing.dataset_loader import load_documents
from preprocessing.chunking import chunk_documents
from embeddings.embedder import get_embedding_model
from vector_db.build_vector_db import build_vector_store

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
# SYSTEM START (RUNS ONCE)
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


# ---------------------------------------------------
# FUNCTION THAT FASTAPI WILL CALL
# ---------------------------------------------------
def run_query(query, dataset=None):

    start = time.time()

    # -----------------------------
    # Query Agent
    # -----------------------------
    print("\n[Query Agent] Checking and correcting query...")
    corrected_query = autocorrect_query(query)

    # -----------------------------
    # Router Agent
    # -----------------------------
    print("[Router Agent] Determining appropriate dataset...")

    if dataset:
        selected_dataset = dataset
    else:
        selected_dataset = choose_dataset(corrected_query)

    print("[Router Agent] Dataset Selected:", selected_dataset)

    # -----------------------------
    # Retriever Agent
    # -----------------------------
    print("[Retriever Agent] Retrieving top relevant documents...")

    if selected_dataset == "business":
        docs, results = retrieve_documents(corrected_query, business_db, selected_dataset)
    else:
        docs, results = retrieve_documents(corrected_query, legal_db, selected_dataset)

    docs = [doc for doc, score in results]

    # -----------------------------
    # Reasoning Agent
    # -----------------------------
    print("[Reasoning Agent] Generating answer from retrieved context...")
    answer = generate_response(corrected_query, docs)

    # -----------------------------
    # Formatter Agent
    # -----------------------------
    print("[Formatter Agent] Formatting response...")
    formatted_answer = format_points(answer)

    # -----------------------------
    # Explainability Agent
    # -----------------------------
    explanations = explainability_agent(results)

    # -----------------------------
    # Evaluation Agent
    # -----------------------------
    metrics = evaluate_rag(corrected_query, formatted_answer, docs, embedding_model)

    end = time.time()

    response_time = round(end - start, 2)

    return {
        "corrected_query": corrected_query,
        "dataset": selected_dataset,
        "documents": [doc.page_content for doc in docs],
        "explanations": explanations,
        "answer": formatted_answer,
        "metrics": metrics,
        "response_time": response_time
    }