from django.core.mail import send_mail
from django.conf import settings


def send_selected_email(candidate_email, candidate_name):

    subject = "Interview Shortlisted"

    message = f"""
Hello {candidate_name},

Congratulations! 

Your resume has been shortlisted by our AI hiring system.

Our HR team will contact you shortly regarding the next steps in the recruitment process.

If you have any questions or need more information, you can ask our AI HR Assistant here:
https://chatbot-6zixpkxpfugd8zpfwheail.streamlit.app/

Best Regards,
HR Team

"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [candidate_email],
        fail_silently=False
    )


def send_rejected_email(candidate_email, candidate_name):

    subject = "Application Status"

    message = f"""
Hello {candidate_name},

Thank you for applying.

After reviewing your resume, we regret to inform you that you were not shortlisted for this position.

We encourage you to apply again in the future.

Best Regards,
HR Team
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [candidate_email],
        fail_silently=False
    )


def forward_resume_to_hr(resume_path):

    subject = "New Candidate Shortlisted"

    message = "A candidate has been shortlisted by the AI system."

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.HR_EMAIL],
        fail_silently=False
    )