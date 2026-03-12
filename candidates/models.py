from django.db import models

# Create your models here.


class Candidate(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=20, blank=True, null=True)

    resume = models.FileField(upload_to="resumes/")

    skills = models.TextField(blank=True, null=True)

    experience = models.TextField(blank=True, null=True)

    ats_score = models.IntegerField(blank=True, null=True)

    status = models.CharField(
        max_length=50,
        default="applied"
    )

    interview_date = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name