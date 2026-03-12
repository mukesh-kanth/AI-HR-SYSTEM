def extract_skills(text):

    skills_database = [
        "python",
        "django",
        "flask",
        "react",
        "node",
        "sql",
        "machine learning",
        "data analysis"
    ]

    detected = []

    text = text.lower()

    for skill in skills_database:
        if skill in text:
            detected.append(skill)

    return detected