#retriever_agent.py
def retrieve_documents(query, db, dataset):

    print("[Retriever Agent] Retrieving documents...")

    if dataset == "business":
        results = db.similarity_search_with_score(
            query,
            k=3,
            filter={"dataset": "business_docs"}
        )

    else:
        results = db.similarity_search_with_score(
            query,
            k=3,
            filter={"dataset": "legal_cases"}
        )

    docs = [doc for doc, score in results]

    return docs, results