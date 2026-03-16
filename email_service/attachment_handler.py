import os
from django.conf import settings


def save_attachment(filename, content):

    try:
        if not filename or not content:
            return None

        upload_dir = os.path.join(settings.MEDIA_ROOT, "resumes")

        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, filename)

        with open(file_path, "wb") as f:
            f.write(content)

        return file_path

    except Exception as e:
        print("Attachment save error:", e)
        return None