from rest_framework import serializers
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "resume",
            "skills",
            "ats_score",
            "created_at"
        ]

        read_only_fields = [
            "skills",
            "ats_score",
            "created_at"
        ]

    def validate_resume(self, value):

        allowed_types = ["pdf", "docx"]

        file_extension = value.name.split(".")[-1].lower()

        if file_extension not in allowed_types:
            raise serializers.ValidationError(
                "Only PDF or DOCX resumes are allowed"
            )

        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError(
                "Resume file must be less than 5MB"
            )

        return value