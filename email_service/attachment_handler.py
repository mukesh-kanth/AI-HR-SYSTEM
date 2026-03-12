import os
from django.conf import settings


def save_attachment(filename, content):

    resume_folder = os.path.join(settings.MEDIA_ROOT, "resumes")

    if not os.path.exists(resume_folder):
        os.makedirs(resume_folder)

    file_path = os.path.join(resume_folder, filename)

    with open(file_path, "wb") as f:
        f.write(content)

    return file_path