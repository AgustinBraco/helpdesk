from django.db import models
from django.utils import timezone


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.ForeignKey(
        "roles.Rol", on_delete=models.CASCADE, related_name="employees"
    )

    class Meta:
        db_table = "employees"


class EmployeeHistory(models.Model):
    ticket = models.ForeignKey(
        "tickets.Ticket", on_delete=models.CASCADE, related_name="employees"
    )
    employee = models.ForeignKey(
        "employees.Employee", on_delete=models.CASCADE, related_name="employees"
    )
    changed_at = models.DateField(default=timezone.now)

    class Meta:
        db_table = "employees_history"
