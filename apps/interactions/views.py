from django.shortcuts import render
from .models import Comment, Visit


def interactions(request):
    return render(request, "interactions.html")


def comments_all(request):
    comments = Comment.objects.all()
    return render(request, "comments_all.html", {"comments": comments})


def visits_all(request):
    visits = Visit.objects.all()
    return render(request, "visits_all.html", {"visits": visits})
