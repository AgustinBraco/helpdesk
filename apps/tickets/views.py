from django.shortcuts import render
from .models import Ticket


def tickets_all(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets/tickets_all.html", {"tickets": tickets})
