from django.shortcuts import render
from .models import Ticket, State, TicketHistory


def tickets(request):
    return render(request, "tickets.html")


def tickets_all(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets_all.html", {"tickets": tickets})


def states_all(request):
    states = State.objects.all()
    return render(request, "states_all.html", {"states": states})


def ticket_history_all(request):
    ticket_history = TicketHistory.objects.all()
    return render(
        request, "ticket_history_all.html", {"ticket_history": ticket_history}
    )
