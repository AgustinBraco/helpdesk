from django.db import models


class Employee(models.Model):
    id_person = models.ForeignKey(
        "users.Person", on_delete=models.CASCADE, related_name="employees"
    )
    id_contact = models.ForeignKey(
        "users.Contact", on_delete=models.CASCADE, related_name="employees"
    )
    tax_id = models.CharField(max_length=15)
    role = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.tax_id}"


class Client(models.Model):
    id_person = models.ForeignKey(
        "users.Person", on_delete=models.CASCADE, related_name="clients"
    )
    id_contact = models.ForeignKey(
        "users.Contact", on_delete=models.CASCADE, related_name="clients"
    )
    id_company = models.ForeignKey(
        "users.Company", on_delete=models.CASCADE, related_name="clients"
    )
    tax_id = models.CharField(max_length=15)
    role = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.tax_id}"
