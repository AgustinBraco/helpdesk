from django.db import models


class Rol(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "roles"


class Permission(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "permissions"


class RolPermission(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="roles")
    permission = models.ForeignKey(
        Permission, on_delete=models.CASCADE, related_name="roles"
    )

    class Meta:
        db_table = "roles_permissions"
