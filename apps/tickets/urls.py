from django.urls import path
from .views import TicketsView, TicketDetailView, TicketCreateView

urlpatterns = [
    path("tickets/", TicketsView.as_view(), name="tickets"),
    path("tickets/<int:id>/", TicketDetailView.as_view(), name="ticket"),
    path("tickets/create/", TicketCreateView.as_view(), name="create"),
]
