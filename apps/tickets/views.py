from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from apps.tickets.models import Ticket
from apps.interactions.models import Comment, Visit

from apps.tickets.models import Ticket


class TicketsView(LoginRequiredMixin, TemplateView):
    template_name = "tickets/tickets.html"


class TicketDetailView(DetailView):
    model = Ticket
    template_name = "tickets/ticket.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ticket = self.get_object()

        context["comments"] = Comment.objects.filter(
            id_history__in=ticket.ticket_history.all()
        )

        context["visits"] = Visit.objects.filter(
            id_history__in=ticket.ticket_history.all()
        )

        context["history"] = ticket.ticket_history.all()

        return context

class TicketCreateView(LoginRequiredMixin, TemplateView):
    template_name = "tickets/create.html"
