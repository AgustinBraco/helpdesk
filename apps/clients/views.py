from django.shortcuts import render
from .models import Client


def clients_all(request):
    clients = Client.objects.all()
    return render(request, "clients_all.html", {"clients": clients})
