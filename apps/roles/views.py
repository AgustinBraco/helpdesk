from django.shortcuts import render
from .models import Rol


def roles_all(request):
    roles = Rol.objects.all()
    return render(request, "roles_all.html", {"roles": roles})
