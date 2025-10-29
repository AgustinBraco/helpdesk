from django.db import models
from django.utils import timezone


class State(models.Model):
    step = models.CharField(max_length=255)

    class Meta:
        db_table = "states"

    def __str__(self):
        return self.step


class StateHistory(models.Model):
    ticket = models.ForeignKey(
        "tickets.Ticket", on_delete=models.CASCADE, related_name="states"
    )
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="states")
    changed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "states_history"

    def __str__(self):
        return f"{self.state} - {self.ticket}"
