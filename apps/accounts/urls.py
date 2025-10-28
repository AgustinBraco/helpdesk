from django.urls import path
from . import views

urlpatterns = [
    path("", views.accounts_all, name="accounts_all"),
]
