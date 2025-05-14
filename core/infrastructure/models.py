from django.db import models


class TaskModel(models.Model):
    PRIORITY_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()
    prioridad = models.CharField(max_length=10, choices=PRIORITY_CHOICES)

    class Meta:
        db_table = 'tasks' 