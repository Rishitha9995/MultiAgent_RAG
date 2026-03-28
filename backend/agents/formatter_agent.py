#formatter_agent.py
def format_points(answer):

    print("[Formatter Agent] Structuring response...")

    sentences = answer.replace("\n", " ").split(".")

    points = []

    for s in sentences:
        s = s.strip()

        if len(s) > 20:
            points.append("• " + s)

    return "\n".join(points[:6])