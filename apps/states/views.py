from django.shortcuts import render
from .models import State


def states_all(request):
    states = State.objects.all()
    return render(request, "states_all.html", {"states": states})
