from django.urls import path
from . import views

urlpatterns = [
    path("", views.roles, name="roles"),
    path("clients/", views.clients_all, name="clients_all"),
    path("employees/", views.employees_all, name="employees_all"),
]
