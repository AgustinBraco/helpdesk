from django.urls import path
from . import views

urlpatterns = [
    path("", views.attachments_all, name="attachments_all"),
]
