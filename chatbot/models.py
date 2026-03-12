from django.db import models

# Create your models here.

class ChatMessage(models.Model):

    candidate_email = models.EmailField()

    message = models.TextField()

    response = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.candidate_email