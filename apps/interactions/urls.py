from django.urls import path
from . import views

urlpatterns = [
    path("", views.interactions, name="interactions"),
    path("comments/", views.comments_all, name="comments_all"),
    path("visits/", views.visits_all, name="visits_all"),
]
