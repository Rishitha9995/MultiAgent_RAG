#explainability_agent.py
def explainability_agent(results):

    explanations = []

    for i, (doc, score) in enumerate(results, 1):

        source = doc.metadata.get("source", "Unknown")

        snippet = doc.page_content[:80].replace("\n", " ")

        reason = f"Selected because this document discusses: {snippet}..."

        explanations.append({
            "rank": i,
            "source": source,
            "score": round(score,3),
            "reason": reason
        })

    return explanations