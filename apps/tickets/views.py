from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket


@login_required
def tickets(request):
    return render(request, "tickets.html")


@login_required
def ticket(request, id):
    ticket = Ticket.objects.filter(id=id).first()

    if ticket is None:
        return redirect("tickets")
    else:
        return render(request, "ticket.html", {"ticket": ticket})


@login_required
def create(request):
    return render(request, "create.html")
