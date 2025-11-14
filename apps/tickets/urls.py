from django.urls import path
from . import views

urlpatterns = [
    path("", views.tickets, name="tickets"),
    path("states/", views.states_all, name="states_all"),
    path("tickets/", views.tickets_all, name="tickets_all"),
    path("ticket_history/", views.ticket_history_all, name="ticket_history_all"),
]
