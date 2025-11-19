from django.db import models
from django.utils import timezone


class Contact(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.email}"


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Company(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}"
