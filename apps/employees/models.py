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

    def __str__(self):
        return self.email


class EmployeeHistory(models.Model):
    ticket = models.ForeignKey(
        "tickets.Ticket", on_delete=models.CASCADE, related_name="employees_history"
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="employees_history"
    )
    changed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "employees_history"

    def __str__(self):
        return f"{self.employee} - {self.ticket}"
