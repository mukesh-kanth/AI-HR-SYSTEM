import re

from resume_parser.parser import extract_text_from_resume
from resume_parser.skills import extract_skills
from resume_parser.ats import calculate_ats_score


from email_service.email_sender import (
    send_selected_email,
    send_rejected_email,
    forward_resume_to_hr
)

def extract_phone(text):

    phone = re.findall(r'\b\d{10}\b', text)

    if phone:
        return phone[0]

    return ""

import re

def extract_phone_number(text):

    """
    Extract phone numbers from resume text
    """

    phone_pattern = r'(\+?\d[\d\s\-]{8,15}\d)'

    matches = re.findall(phone_pattern, text)

    if matches:
        phone = matches[0]

        # remove spaces and dashes
        phone = phone.replace(" ", "").replace("-", "")

        return phone

    return "Not Found"


def process_resume(candidate):

    resume_path = candidate.resume.path

    # Extract text
    resume_text = extract_text_from_resume(resume_path)

      # Extract phone
    phone = extract_phone_number(resume_text)


    # Extract skills
    skills = extract_skills(resume_text)

    # Calculate ATS
    ats_score = calculate_ats_score(resume_text, skills)

    # Update candidate
    candidate.phone = phone
    candidate.skills = ", ".join(skills)
    candidate.ats_score = ats_score

    candidate.save()

    # Decision logic
    if ats_score >= 70:

        forward_resume_to_hr(resume_path)

        send_selected_email(
            candidate.email,
            candidate.name
        )

    else:

        send_rejected_email(
            candidate.email,
            candidate.name
        )

    return candidate