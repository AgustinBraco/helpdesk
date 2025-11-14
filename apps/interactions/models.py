from django.db import models
from django.utils import timezone


class Comment(models.Model):
    id_history = models.ForeignKey(
        "tickets.TicketHistory", on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.content}"


class Visit(models.Model):
    id_history = models.ForeignKey(
        "tickets.TicketHistory", on_delete=models.CASCADE, related_name="visits"
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"

    def __str__(self):
        return f"{self.content}"
