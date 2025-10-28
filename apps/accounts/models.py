from django.db import models


class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=266)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
