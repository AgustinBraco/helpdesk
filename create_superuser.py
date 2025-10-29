import os
import django
from django.contrib.auth.models import User
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
EMAIL = os.environ.get("EMAIL")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helpdesk.settings")
django.setup()

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(
        username=USERNAME,
        email=EMAIL,
        password=PASSWORD,
    )
    print("Superuser created")
else:
    print("Superuser already exist")
