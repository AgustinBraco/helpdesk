from django.shortcuts import render
from .models import File


def files_all(request):
    files = File.objects.all()
    return render(request, "files_all.html", {"files": files})
