from django.db import models
from django.utils import timezone


class Attachment(models.Model):
    id_history = models.ForeignKey(
        "tickets.TicketHistory", on_delete=models.CASCADE, related_name="attachments"
    )
    content = models.FileField(upload_to="files/%Y%m%d/")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Attachment"
        verbose_name_plural = "Attachments"

    def __str__(self):
        return f"{self.content}"
