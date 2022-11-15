from django.db import models

# Create your models here.
class Priority(models.Model):
    """
        Modelo para manejar el catálogo de Prioridades
        Ejemplos: 
        1. Baja
        2. Media
        3. Alta
    """
    name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    title = models.CharField(max_length=60, null = False)
    description = models.CharField(max_length=150, null = True, blank = True)
    is_completed = models.BooleanField(default=False)
    priority = models.ForeignKey(Priority, on_delete=models.DO_NOTHING)


    def __str__(self):
        return f"{self.title} - {self.description}"