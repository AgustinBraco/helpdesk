from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    id_client = models.ForeignKey(
        "roles.Client", on_delete=models.PROTECT, related_name="tickets"
    )
    priority = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return f"{self.title}"


class State(models.Model):
    id_ticket = models.ForeignKey(
        Ticket, on_delete=models.PROTECT, related_name="states"
    )
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return f"{self.state}"


class TicketHistory(models.Model):
    id_ticket = models.ForeignKey(
        Ticket, on_delete=models.PROTECT, related_name="ticket_history"
    )
    id_employee = models.ForeignKey(
        "roles.Employee", on_delete=models.PROTECT, related_name="ticket_history"
    )
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "TicketHistory"
        verbose_name_plural = "TicketHistory"

    def __str__(self):
        return f"{self.timestamp}"
