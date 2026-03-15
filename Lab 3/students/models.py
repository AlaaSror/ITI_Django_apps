from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    student_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} - Age: {self.age} - ID: {self.student_id}"