from django.db import models
from instructors.models import Instructor
from students.models import Student

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    students = models.ManyToManyField(Student, related_name='courses', blank=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, related_name='courses')
    
    def __str__(self):
        return f"{self.name} ({self.code})"