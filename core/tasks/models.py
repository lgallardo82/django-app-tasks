from django.db import models

# Create your models here.
class Priority(models.Model):
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