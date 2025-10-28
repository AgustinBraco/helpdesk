from django.shortcuts import render
from .models import Account


def accounts_all(request):
    accounts = Account.objects.all()
    return render(request, "accounts_all.html", {"accounts": accounts})
