from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name="users"),
    path("companies/", views.companies_all, name="companies_all"),
    path("contacts/", views.contacts_all, name="contacts_all"),
    path("persons/", views.persons_all, name="persons_all"),
]
