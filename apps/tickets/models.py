from django.db import models


class Ticket(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=266)
    description = models.CharField(max_length=266)

    def __str__(self):
        return f"Ticket N°{self.id}: {self.title}"

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
