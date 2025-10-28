from django.db import models


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=266)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
