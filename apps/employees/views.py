from django.shortcuts import render
from .models import Employee


def employees_all(request):
    employees = Employee.objects.all()
    return render(request, "employees_all.html", {"employees": employees})
