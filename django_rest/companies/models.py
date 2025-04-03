from django.db import models

# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=50)
    CEO = models.CharField(max_length=50)
    established_at = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name