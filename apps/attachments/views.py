from django.shortcuts import render
from .models import Attachment


def attachments_all(request):
    attachments = Attachment.objects.all()
    return render(request, "attachments_all.html", {"attachments": attachments})
