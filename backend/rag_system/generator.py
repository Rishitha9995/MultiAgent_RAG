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


# from transformers import pipeline

# generator = pipeline(
#     "text-generation",  
#     model="google/flan-t5-base",
#     max_length=256
# )

# def generate_answer(query, docs):

#     context = "\n".join([d.page_content for d in docs[:3]])  # limit to top 3 docs for context

#     prompt = f"""
# You are an assistant that answers questions using the provided context.

# Context:
# {context}

# Question:
# {query}

# Provide a clear and concise answer in 4-6 bullet points.
# Do not repeat the instructions.
# """

#     result = generator(prompt)[0]["generated_text"]

#     return result.strip()