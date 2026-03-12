import imaplib
import email
from django.conf import settings

from email_service.attachment_handler import save_attachment
from candidates.models import Candidate
from candidates.services import process_resume


def read_resume_emails():

    try:
        print("Connecting to Gmail...")

        mail = imaplib.IMAP4_SSL("imap.gmail.com")

        mail.login(
            settings.EMAIL_HOST_USER,
            settings.EMAIL_HOST_PASSWORD
        )

        mail.select("inbox")

        status, messages = mail.search(None, "UNSEEN")

        email_ids = messages[0].split()

        print(f"Found {len(email_ids)} new emails")

        for mail_id in email_ids:

            status, msg_data = mail.fetch(mail_id, "(RFC822)")

            for response_part in msg_data:

                if isinstance(response_part, tuple):

                    msg = email.message_from_bytes(response_part[1])

                    sender = email.utils.parseaddr(msg["From"])[1]

                    print("Processing email from:", sender)

                    for part in msg.walk():

                        if part.get_content_disposition() == "attachment":

                            filename = part.get_filename()

                            if not filename:
                                continue

                            content = part.get_payload(decode=True)

                            file_path = save_attachment(filename, content)

                            candidate = Candidate.objects.create(
                                name=sender.split("@")[0],
                                email=sender,
                                phone="0000000000",
                                resume=file_path.replace(
                                    settings.MEDIA_ROOT + "\\",
                                    ""
                                )
                            )

                            process_resume(candidate)

        mail.logout()

        print("Email processing completed")

    except Exception as e:

        print("Error reading emails:", e)