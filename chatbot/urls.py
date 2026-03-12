from django.urls import path
from . import views
urlpatterns = [

    path("", views.chatbot_ui, name="chatbot-ui"),   
    
    path("chat/", views.chatbot_api, name="chatbot-api"),

]