from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    athor = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name