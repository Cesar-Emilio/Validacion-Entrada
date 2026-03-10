from django.db import models


class Universidad(models.Model):

    nombre_completo = models.CharField(
        max_length=100,
        verbose_name="Nombre completo"
    )

    matricula = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="Matrícula UTEZ"
    )

    correo = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name="Correo institucional"
    )

    telefono = models.CharField(
        max_length=10,
        verbose_name="Teléfono móvil"
    )

    rfc = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="RFC"
    )

    contra = models.CharField(
        max_length=255,
        verbose_name="Contraseña"
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "universidad"
        verbose_name = "Universitario"
        verbose_name_plural = "Universitarios"

    def __str__(self):
        return f"{self.nombre_completo} - {self.matricula}"