from django.db import models
from django.utils import timezone


class Client(models.Model):
    tax_id = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    role = models.ForeignKey(
        "roles.Rol", on_delete=models.CASCADE, related_name="clients"
    )

    class Meta:
        db_table = "clients"

    def __str__(self):
        return self.tax_id


class Company(Client):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "companies"

    def __str__(self):
        return self.name


class Person(Client):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(default=timezone.now)

    class Meta:
        db_table = "persons"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
