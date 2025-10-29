from django.db import models


class Rol(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "roles"

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "permissions"

    def __str__(self):
        return self.name


class RolPermission(models.Model):
    rol = models.ForeignKey(
        Rol, on_delete=models.CASCADE, related_name="roles_permissions"
    )
    permission = models.ForeignKey(
        Permission, on_delete=models.CASCADE, related_name="roles_permissions"
    )

    class Meta:
        db_table = "roles_permissions"

    def __str__(self):
        return f"{self.rol}"
