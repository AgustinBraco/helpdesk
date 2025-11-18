from django.db import models
from django.core.exceptions import ValidationError


class Employee(models.Model):
    id_contact = models.ForeignKey(
        "users.Contact", on_delete=models.PROTECT, related_name="employees"
    )
    id_person = models.ForeignKey(
        "users.Person", on_delete=models.PROTECT, related_name="employees"
    )
    tax_id = models.CharField(max_length=15)
    role = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.tax_id}"


class Client(models.Model):
    id_contact = models.ForeignKey(
        "users.Contact", on_delete=models.PROTECT, related_name="clients"
    )
    id_person = models.ForeignKey(
        "users.Person",
        on_delete=models.PROTECT,
        related_name="clients",
        null=True,
        blank=True,
    )
    id_company = models.ForeignKey(
        "users.Company",
        on_delete=models.PROTECT,
        related_name="clients",
        null=True,
        blank=True,
    )
    tax_id = models.CharField(max_length=15)
    role = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def clean(self):
        if not self.id_person and not self.id_company:
            raise ValidationError("Debe completar id_person o id_company.")

        if self.id_person and self.id_company:
            raise ValidationError("No puede completar ambos: id_person o id_company.")

    def __str__(self):
        return f"{self.tax_id}"
