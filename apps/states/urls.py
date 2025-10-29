from django.urls import path
from . import views

urlpatterns = [
    path("", views.states_all, name="states_all"),
]
