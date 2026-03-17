#action_engine.py
def perform_action(query):

    if "contract" in query.lower():
        return "Suggested Action: Prepare a legal contract document."

    elif "startup" in query.lower():
        return "Suggested Action: Register business and prepare legal documentation."

    elif "compliance" in query.lower():
        return "Suggested Action: Review regulatory compliance requirements."

    else:
        return "No automated action required."