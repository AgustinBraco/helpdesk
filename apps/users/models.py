from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=266)
    last_name = models.CharField(max_length=266)
    nickname = models.CharField(max_length=266)
    rol = models.CharField(max_length=266)

    def __str__(self):
        return f"User N°{self.id}: {self.nickname}"
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

