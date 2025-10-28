from django.db import models


class Visit(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=266)

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"
