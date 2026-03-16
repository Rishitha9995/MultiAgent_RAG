#evaluate_rag_agent.py
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_rag(query, answer, docs, embedding_model):

    print("\n[Evaluation Agent] Evaluating RAG performance...")

    context = " ".join([d.page_content for d in docs])

    q_emb = embedding_model.embed_query(query)
    a_emb = embedding_model.embed_query(answer)
    c_emb = embedding_model.embed_query(context)

    ans_sim = cosine_similarity([a_emb], [c_emb])[0][0]
    qry_sim = cosine_similarity([q_emb], [c_emb])[0][0]

    coverage = min(len(answer) / max(len(context), 1), 1)

    confidence = (ans_sim + qry_sim) / 2

    print("\n--- RAG Evaluation Metrics ---")
    print("Answer-Context Similarity:", round(ans_sim, 3))
    print("Query-Context Relevance:", round(qry_sim, 3))
    print("Context Coverage:", round(coverage, 3))

    if confidence > 0.75:
        print("Confidence Level: High")
    elif confidence > 0.5:
        print("Confidence Level: Medium")
    else:
        print("Confidence Level: Low")