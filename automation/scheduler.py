import os
import sys
import django
import schedule
import time

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Setup Django
django.setup()

from email_service.email_reader import read_resume_emails


def job():
    print("Checking for new resume emails...")
    try:
        read_resume_emails()
        print("Email check completed.")
    except Exception as e:
        print("Error:", e)


# Run every 2 minutes
schedule.every(2).minutes.do(job)

print("📧 Resume Email Auto Reader Started...")

while True:
    schedule.run_pending()
    time.sleep(5)