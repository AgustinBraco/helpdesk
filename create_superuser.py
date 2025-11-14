import os
import django

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

SU_USERNAME = os.environ.get("SU_USERNAME")
SU_PASSWORD = os.environ.get("SU_PASSWORD")
SU_EMAIL = os.environ.get("SU_EMAIL")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helpdesk.settings")
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username=SU_USERNAME).exists():
    User.objects.create_superuser(
        username=SU_USERNAME,
        email=SU_EMAIL,
        password=SU_PASSWORD,
    )
    print("Superuser created")
else:
    print("Superuser already exist")
