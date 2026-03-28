#chunking.py
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# def chunk_documents(documents):

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     chunks = splitter.create_documents(documents)

#     return chunks

# chunking.py

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = []
    chunk_counter = 0

    for doc in documents:

        # Split document text
        split_texts = splitter.split_text(doc.page_content)

        for text in split_texts:

            chunk = Document(
                page_content=text,
                metadata={
                    **doc.metadata,              # preserve original metadata
                    "chunk_id": chunk_counter,   # unique chunk identifier
                    "chunk_length": len(text)    # length of chunk
                }
            )

            chunks.append(chunk)
            chunk_counter += 1

    print(f"Created {len(chunks)} chunks from {len(documents)} documents")

    return chunks