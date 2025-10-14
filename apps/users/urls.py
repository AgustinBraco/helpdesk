from django.urls import path
from . import views

urlpatterns = [
    path("", views.users_all, name="users_all"),
]
