def detect_intent(message):

    if not message:
        return "unknown"

    message = message.lower()

    if "interview" in message:
        return "interview_schedule"

    elif "next round" in message:
        return "next_round"

    elif "documents" in message:
        return "documents_required"

    elif "salary" in message:
        return "salary"

    elif "location" in message:
        return "location"

    return "unknown"