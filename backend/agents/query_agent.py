#query_agent.py
from textblob import TextBlob

def autocorrect_query(query):

    print("[Query Agent] Understanding query...")

    corrected = str(TextBlob(query).correct())

    if corrected.lower() != query.lower():
        print("Auto-corrected query:", corrected)

    return corrected