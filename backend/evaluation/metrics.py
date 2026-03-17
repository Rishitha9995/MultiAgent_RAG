#metrics.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_metrics(answer, docs):

    context = ""

    for doc in docs:
        context += doc.page_content + " "

    texts = [answer, context]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    context_coverage = min(1.0, similarity + 0.1)

    if similarity > 0.75:
        confidence = "High"
    elif similarity > 0.5:
        confidence = "Medium"
    else:
        confidence = "Low"

    return similarity, context_coverage, confidence
