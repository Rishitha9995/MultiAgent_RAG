#reasoning_agent.py
from rag_system.generator import generate_answer

def generate_response(query, docs):

    print("[Reasoning Agent] Generating answer...")

    answer = generate_answer(query, docs)

    return answer