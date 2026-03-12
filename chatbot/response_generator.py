from .knowledge_base import FAQ_RESPONSES
from .intent_detector import detect_intent


def generate_response(message):

    intent = detect_intent(message)

    if intent in FAQ_RESPONSES:
        return FAQ_RESPONSES[intent]

    return "Sorry, I couldn't understand your question."