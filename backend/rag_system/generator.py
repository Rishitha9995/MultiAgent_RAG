#generator.py
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_length=256
)

def generate_answer(query, docs):

    context = "\n".join([d.page_content for d in docs[:3]])  # limit to top 3 docs for context

    prompt = f"""
Answer the question using ONLY the context.

Context:
{context}

Question:
{query}

Answer briefly.
"""

    return generator(prompt)[0]["generated_text"]


