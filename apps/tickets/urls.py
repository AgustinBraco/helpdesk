from django.urls import path
from .views import tickets, ticket, create

urlpatterns = [
    path("", tickets, name="tickets"),
    path("<int:id>/", ticket, name="ticket"),
    path("create/", create, name="create"),
]
