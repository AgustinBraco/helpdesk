from django.shortcuts import render
from .models import User


def users_all(request):
    users = User.objects.all()
    return render(request, "users/users_all.html", {"users": users})
