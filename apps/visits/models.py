from django.db import models
from django.utils import timezone


class Visit(models.Model):
    ticket = models.ForeignKey(
        "tickets.Ticket", on_delete=models.CASCADE, related_name="visits"
    )
    employee = models.ForeignKey(
        "employees.Employee", on_delete=models.CASCADE, related_name="visits"
    )
    content = models.TextField()
    created_at = models.DateField(default=timezone.now)

    class Meta:
        db_table = "visits"
