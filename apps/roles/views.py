from django.shortcuts import render
from .models import Employee, Client


def roles(request):
    return render(request, "roles.html")


def employees_all(request):
    employees = Employee.objects.all()
    return render(request, "employees_all.html", {"employees": employees})


def clients_all(request):
    clients = Client.objects.all()
    return render(request, "clients_all.html", {"clients": clients})
