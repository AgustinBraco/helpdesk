from django.urls import path
from . import views

urlpatterns = [
    path("", views.files_all, name="files_all"),
]
