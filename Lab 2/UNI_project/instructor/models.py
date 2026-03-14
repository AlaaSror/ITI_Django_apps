from django.db import models

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    courses = models.OneToOneField('courses.Course', related_name='instructors', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.email}"