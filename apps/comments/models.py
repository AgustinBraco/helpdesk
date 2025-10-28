from django.db import models


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=266)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
