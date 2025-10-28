from django.db import models


class File(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=266)

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
