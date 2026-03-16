#router_agent.py
def choose_dataset(query):

    print("[Router Agent] Selecting dataset...")

    query = query.lower()

    business_words = [
        "business","startup","company","registration","gst",
        "tax","funding","license","profit","market",
        "entrepreneur","incorporation","business plan",
        "business law","enterprise"
    ]

    legal_words = [
        "court","case","judge","lawsuit","litigation",
        "criminal","civil","lawyer","agreement",
        "contract","legal dispute","legal rights"
    ]

    for w in business_words:
        if w in query:
            print("Dataset: business")
            return "business"

    for w in legal_words:
        if w in query:
            print("Dataset: legal")
            return "legal"

    return "business"