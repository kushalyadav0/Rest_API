from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name
    