from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import os


# -----------------------------
# 1️⃣ Resume Received Email
# -----------------------------
def send_auto_reply(email, name):

    subject = "Application Received"

    message = f"""
Hello {name},

Thank you for applying.

Your resume has been successfully received and is being reviewed by our AI HR system.

Best Regards
HR Team
"""

    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])


# -----------------------------
# 2️⃣ Shortlisted Email
# -----------------------------
def send_selected_email(email, name):

    subject = "Application Shortlisted"

    message = f"""
Hello {name},

Congratulations!

Your resume has been shortlisted by our AI hiring system.

Our HR team will contact you shortly.

If you have questions you can ask our HR chatbot:
https://chatbot-6zixpkxpfugd8zpfwheail.streamlit.app/

Best Regards
HR Team
"""

    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])


# -----------------------------
# 3️⃣ Rejected Email
# -----------------------------
def send_rejected_email(email, name):

    subject = "Application Update"

    message = f"""
Hello {name},

Thank you for applying.

After reviewing your resume, we regret to inform you that you were not selected for this position.

We encourage you to apply again in the future.

Best Regards
HR Team
"""

    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])


# -----------------------------
# 4️⃣ Forward Resume to HR
# -----------------------------
def forward_resume_to_hr(candidate):

    try:

        subject = f"New Candidate Resume: {candidate.name}"

        message = f"""
A new candidate has applied.

Name: {candidate.name}
Email: {candidate.email}

Please review the attached resume.
"""

        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.HR_EMAIL]  # HR email in settings.py
        )

        if candidate.resume:
            resume_path = os.path.join(settings.MEDIA_ROOT, candidate.resume.name)
            email.attach_file(resume_path)

        email.send()

        print("Resume forwarded to HR")

    except Exception as e:
        print("Error forwarding resume:", e)