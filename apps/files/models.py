from django.db import models
from django.utils import timezone


class File(models.Model):
    ticket = models.ForeignKey(
        "tickets.Ticket", on_delete=models.CASCADE, related_name="files"
    )
    content = models.FileField(upload_to="files/%Y%m%d/")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "files"

    def __str__(self):
        return self.content.name
