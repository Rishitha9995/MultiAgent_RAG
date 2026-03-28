#dataset_loader.py

import os
from langchain_core.documents import Document

def load_documents(folder_path):

    documents = []

    if not os.path.exists(folder_path):
        print("Folder not found:", folder_path)
        return documents

    # Detect dataset type from folder name
    dataset_type = os.path.basename(folder_path)

    for file in os.listdir(folder_path):

        if file.endswith(".txt"):

            file_path = os.path.join(folder_path, file)

            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            doc = Document(
                page_content=text,
                metadata={
                    "source": file,
                    "dataset": dataset_type,
                    "file_path": file_path,
                    "doc_length": len(text)
                }
            )

            documents.append(doc)

    print(f"Loaded {len(documents)} documents from {folder_path}")

    return documents