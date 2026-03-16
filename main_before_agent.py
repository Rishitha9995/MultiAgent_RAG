#main.py
import os
import time
from textblob import TextBlob
from sklearn.metrics.pairwise import cosine_similarity

from preprocessing.dataset_loader import load_documents
from preprocessing.chunking import chunk_documents
from embeddings.embedder import get_embedding_model
from vector_db.build_vector_db import build_vector_store
from rag_system.retriever import retrieve_documents
from rag_system.generator import generate_answer


# -----------------------------
# AUTO SPELL CORRECTION
# -----------------------------
def autocorrect_query(query):

    corrected = str(TextBlob(query).correct())

    if corrected.lower() != query.lower():
        print("\nAuto-corrected query:", corrected)

    return corrected


# -----------------------------
# QUERY ROUTER
# -----------------------------
def choose_dataset(query):

    query = query.lower()

    business_words = [
        "business","startup","company","registration","gst",
        "tax","funding","license","profit","market",
        "entrepreneur","incorporation","business plan",
        "business law","enterprise"
    ]

    legal_words = [
        "court","case","judge","lawsuit","litigation",
        "criminal","civil","lawyer","agreement",
        "contract","legal dispute","legal rights"
    ]

    for w in business_words:
        if w in query:
            return "business"

    for w in legal_words:
        if w in query:
            return "legal"

    return "business"


# -----------------------------
# FORMAT ANSWER TO BULLETS
# -----------------------------
def format_points(answer):

    sentences = answer.replace("\n", " ").split(".")

    points = []

    for s in sentences:
        s = s.strip()
        if len(s) > 20:
            points.append("• " + s)

    return "\n".join(points[:6])


# -----------------------------
# RAG METRICS
# -----------------------------
def evaluate_rag(query, answer, docs, embedding_model):

    context = " ".join([d.page_content for d in docs])

    q_emb = embedding_model.embed_query(query)
    a_emb = embedding_model.embed_query(answer)
    c_emb = embedding_model.embed_query(context)

    ans_sim = cosine_similarity([a_emb], [c_emb])[0][0]
    qry_sim = cosine_similarity([q_emb], [c_emb])[0][0]

    coverage = min(len(answer) / max(len(context),1),1)

    confidence = (ans_sim + qry_sim) / 2

    print("\n--- RAG Evaluation Metrics ---")
    print("Answer-Context Similarity:", round(ans_sim,3))
    print("Query-Context Relevance:", round(qry_sim,3))
    print("Context Coverage:", round(coverage,3))

    if confidence > 0.75:
        print("Confidence Level: High")
    elif confidence > 0.5:
        print("Confidence Level: Medium")
    else:
        print("Confidence Level: Low")


# -----------------------------
# INITIALIZATION
# -----------------------------
print("\nInitializing Multi-Source RAG System...\n")

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

    query = autocorrect_query(query)

    start = time.time()

    dataset = choose_dataset(query)

    print("\nSearching in:", dataset, "dataset")

    # if dataset == "business":
    #     docs = retrieve_documents(query, business_db)
    # else:
    #     docs = retrieve_documents(query, legal_db)

    if dataset == "business":
        results = business_db.similarity_search_with_score(
            query,
            k=3,
            filter={"dataset": "business_docs"}
        )

    else:
        results = legal_db.similarity_search_with_score(
            query,
            k=3,
            filter={"dataset": "legal_cases"}
        )

    # separate documents and scores
    docs = [doc for doc, score in results]

    answer = generate_answer(query, docs)

    answer = format_points(answer)

    end = time.time()

    print("\nAnswer:\n")
    print(answer)

    print("\nTop Retrieved Documents:\n")

    for i, (doc, score) in enumerate(results, 1):

        source = doc.metadata.get("source", "Unknown")

        content_snippet = doc.page_content[:80].replace("\n", " ")

        reason = f"Selected because this document discusses: {content_snippet}..."

        print(f"{i}. {source}")
        print(f"   similarity_score: {round(score,3)}")
        print(f"   reason: {reason}")
        print()

    # print("\nTop Retrieved Documents:")
    # sources = set()
    # for doc, score in results:

    #     print(
    #         f"{doc.metadata.get('source','Unknown')} "
    #         f"(similarity_score: {round(score,3)})"
    #     )

    # for d in docs:
    #     sources.add(d.metadata.get("source", "Unknown"))

    # for s in sources:
    #     print("-", s)

    evaluate_rag(query, answer, docs, embedding_model)

    print("Response Time:", round(end-start,2), "seconds")