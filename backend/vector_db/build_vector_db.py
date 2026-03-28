#build_vector_db.py
from langchain_community.vectorstores import FAISS
import os

def build_vector_store(chunks, embedding_model, save_path):

    # If vector database already exists → load it
    if os.path.exists(save_path):

        print("Loading existing vector database:", save_path)

        vector_store = FAISS.load_local(
            save_path,
            embedding_model,
            allow_dangerous_deserialization=True
        )

        return vector_store

    # Otherwise create new vector DB
    print("Creating new vector database:", save_path)

    vector_store = FAISS.from_documents(
        chunks,
        embedding_model
    )

    # Save vector DB
    vector_store.save_local(save_path)

    print("Vector database saved:", save_path)

    return vector_store
