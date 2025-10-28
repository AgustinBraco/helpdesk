from django.shortcuts import render
from .models import Comment


def comments_all(request):
    comments = Comment.objects.all()
    return render(request, "comments_all.html", {"comments": comments})
