import imaplib
import email
import os
from django.conf import settings

from email_service.attachment_handler import save_attachment
from candidates.models import Candidate
from candidates.services import process_resume


def read_resume_emails():
    mail = None

    try:
        print("📧 Connecting to Gmail...")

        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(
            settings.EMAIL_HOST_USER,
            settings.EMAIL_HOST_PASSWORD
        )

        mail.select("inbox")

        status, messages = mail.search(None, "UNSEEN")

        email_ids = messages[0].split()

        print(f"📨 Found {len(email_ids)} new emails")

        for mail_id in email_ids:

            status, msg_data = mail.fetch(mail_id, "(RFC822)")

            for response_part in msg_data:

                if not isinstance(response_part, tuple):
                    continue

                msg = email.message_from_bytes(response_part[1])

                sender = email.utils.parseaddr(msg.get("From", ""))[1]

                if not sender:
                    print("⚠ Sender not found, skipping email")
                    continue

                print("Processing email from:", sender)

                for part in msg.walk():

                    if part.get_content_disposition() != "attachment":
                        continue

                    filename = part.get_filename()

                    if not filename:
                        print("⚠ Attachment has no filename")
                        continue

                    content = part.get_payload(decode=True)

                    if not content:
                        print("⚠ Attachment content empty")
                        continue

                    file_path = save_attachment(filename, content)

                    if not file_path:
                        print("⚠ Failed to save attachment")
                        continue

                    print("✅ Saved attachment:", file_path)

                    resume_path = os.path.relpath(
                        file_path,
                        settings.MEDIA_ROOT
                    ).replace("\\", "/")

                    candidate = Candidate.objects.filter(email=sender).first()

                    if not candidate:
                        candidate = Candidate.objects.create(
                            name=sender.split("@")[0],
                            email=sender,
                            phone="0000000000",
                            resume=resume_path
                        )
                    else:
                        # update resume if new one received
                        candidate.resume = resume_path
                        candidate.save()

                    process_resume(candidate)

        print("✅ Email processing completed")

    except Exception as e:
        import traceback
        print("❌ Error reading emails:", e)
        traceback.print_exc()

    finally:
        if mail:
            try:
                mail.logout()
            except:
                pass