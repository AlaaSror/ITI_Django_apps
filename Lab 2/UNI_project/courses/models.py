from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    students = models.ManyToManyField('students.Student', related_name='courses')

    def __str__(self):
        return f"{self.code} - {self.name}"