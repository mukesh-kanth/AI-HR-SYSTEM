import re

# Job requirement keywords
JOB_KEYWORDS = [
    "python",
    "django",
    "machine learning",
    "sql",
    "rest api",
    "git",
    "docker",
    "react"
]

TOOLS = [
    "git",
    "docker",
    "jira",
    "github",
    "postman",
    "aws"
]

SECTIONS = [
    "skills",
    "projects",
    "experience",
    "education",
    "certifications"
]


def keyword_score(resume_text):

    score = 0

    for keyword in JOB_KEYWORDS:
        if keyword in resume_text.lower():
            score += 3

    return min(score, 20)


def skill_score(skills):

    score = len(skills) * 5

    return min(score, 25)


def experience_score(resume_text):

    years = re.findall(r'(\d+)\s+years?', resume_text.lower())

    if years:
        years = int(years[0])

        if years >= 5:
            return 15
        elif years >= 3:
            return 10
        elif years >= 1:
            return 5

    return 0


def project_score(resume_text):

    if "project" in resume_text.lower():
        return 10

    return 0


def tools_score(resume_text):

    score = 0

    for tool in TOOLS:
        if tool in resume_text.lower():
            score += 2

    return min(score, 10)


def section_score(resume_text):

    score = 0

    for section in SECTIONS:
        if section in resume_text.lower():
            score += 2

    return min(score, 10)


def contact_score(resume_text):

    email_pattern = r'\S+@\S+'
    phone_pattern = r'\b\d{10}\b'

    email = re.findall(email_pattern, resume_text)
    phone = re.findall(phone_pattern, resume_text)

    if email and phone:
        return 5

    return 0


def resume_length_score(resume_text):

    word_count = len(resume_text.split())

    if 300 <= word_count <= 800:
        return 5

    return 2


def calculate_ats_score(resume_text, skills):

    score = 0

    score += skill_score(skills)
    score += keyword_score(resume_text)
    score += experience_score(resume_text)
    score += project_score(resume_text)
    score += tools_score(resume_text)
    score += section_score(resume_text)
    score += contact_score(resume_text)
    score += resume_length_score(resume_text)

    return min(score, 100)