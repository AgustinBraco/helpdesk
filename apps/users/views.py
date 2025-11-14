from django.shortcuts import render
from .models import Person, Contact, Company


def users(request):
    return render(request, "users.html")


def persons_all(request):
    persons = Person.objects.all()
    return render(request, "persons_all.html", {"persons": persons})


def contacts_all(request):
    contacts = Contact.objects.all()
    return render(request, "contacts_all.html", {"contacts": contacts})


def companies_all(request):
    companies = Company.objects.all()
    return render(request, "companies_all.html", {"companies": companies})
