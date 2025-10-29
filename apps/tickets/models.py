from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    state = models.ForeignKey(
        "states.State", on_delete=models.CASCADE, related_name="tickets"
    )
    employee = models.ForeignKey(
        "employees.Employee", on_delete=models.CASCADE, related_name="tickets"
    )
    client = models.ForeignKey(
        "clients.Client", on_delete=models.CASCADE, related_name="tickets"
    )
    prority = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(default=timezone.now)
    closed_at = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "tickets"
