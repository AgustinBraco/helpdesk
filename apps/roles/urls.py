from django.urls import path
from . import views

urlpatterns = [
    path("", views.roles_all, name="roles_all"),
]
