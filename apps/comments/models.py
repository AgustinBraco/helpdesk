from django.db import models
from django.utils import timezone


class Comment(models.Model):
    ticket = models.ForeignKey(
        "tickets.Ticket", on_delete=models.CASCADE, related_name="comments"
    )
    employee = models.ForeignKey(
        "employees.Employee", on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()
    created_at = models.DateField(default=timezone.now)

    class Meta:
        db_table = "comments"
