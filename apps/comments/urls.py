from django.urls import path
from . import views

urlpatterns = [
    path("", views.comments_all, name="comments_all"),
]
