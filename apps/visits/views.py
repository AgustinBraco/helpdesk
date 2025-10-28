from django.shortcuts import render
from .models import Visit


def visits_all(request):
    visits = Visit.objects.all()
    return render(request, "visits_all.html", {"visits": visits})
