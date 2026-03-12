from rest_framework import viewsets
from .models import Candidate
from .serializers import CandidateSerializer
from .services import process_resume


class CandidateViewSet(viewsets.ModelViewSet):

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def perform_create(self, serializer):

        candidate = serializer.save()

        process_resume(candidate)
        
from django.shortcuts import render
from .models import Candidate

def dashboard(request):

    search = request.GET.get('search')

    if search:
        candidates = Candidate.objects.filter(name__icontains=search)
    else:
        candidates = Candidate.objects.all().order_by('-ats_score')

    return render(request,'dashboard.html',{'candidates':candidates}) 