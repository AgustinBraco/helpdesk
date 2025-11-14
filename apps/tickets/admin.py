from django.contrib import admin
from .models import Ticket, State, TicketHistory

admin.site.register(Ticket)
admin.site.register(State)
admin.site.register(TicketHistory)
