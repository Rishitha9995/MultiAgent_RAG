#retriever.py
def retrieve_documents(query, vector_db, k=3):
    return vector_db.similarity_search(query, k=k)