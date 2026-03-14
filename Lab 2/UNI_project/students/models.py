from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=10, primary_key=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.id} - {self.age}"