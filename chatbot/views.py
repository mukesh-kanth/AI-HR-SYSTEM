from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .ai_engine import generate_ai_response

from .models import ChatMessage


def chatbot_ui(request):
    return render(request, "chatbot.html")


@csrf_exempt
def chatbot_api(request):

    if request.method == "POST":

        try:
            data = json.loads(request.body.decode("utf-8"))
        except:
            data = {}

        message = data.get("message", "")

        if not message:
            return JsonResponse({"response": "Please enter a message."})

        ai_reply = generate_ai_response(message)

        return JsonResponse({"response": ai_reply})

    return JsonResponse({"error": "Invalid request"})