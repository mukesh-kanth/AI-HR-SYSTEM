from celery import shared_task


@shared_task
def process_resume(candidate_id):

    from candidates.models import Candidate
    from resume_parser.ats import calculate_score

    candidate = Candidate.objects.get(id=candidate_id)

    with open(candidate.resume.path) as f:

        text = f.read()

    score = calculate_score(text)

    candidate.ats_score = score

    if score > 70:
        candidate.status = "selected"
    else:
        candidate.status = "rejected"

    candidate.save()
    
from email_service.email_reader import read_resume_emails


def check_inbox():

    print("Checking inbox for resumes...")

    read_resume_emails()

    print("Inbox check completed.")    