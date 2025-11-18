from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ticket


class TicketsView(LoginRequiredMixin, TemplateView):
    template_name = "tickets/tickets.html"


class TicketDetailView(LoginRequiredMixin, TemplateView):
    template_name = "tickets/ticket.html"

    def get(self, request, id):
        ticket = Ticket.objects.filter(id=id).first()
        if ticket is None:
            return redirect("tickets")
        return self.render_to_response({"ticket": ticket})


class TicketCreateView(LoginRequiredMixin, TemplateView):
    template_name = "tickets/create.html"
