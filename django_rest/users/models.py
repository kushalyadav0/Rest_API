from django.db import models

# Create your models here.
"""
class User(models.Model):
    username = models.a
    first_name = models.a
    last_name = models.a
    email = models.a
    password = models.a    

    def __str__(self):
        return self.username 
   pass """

class SignUp(models.Model):
   username = models.CharField(max_length=12)
   email = models.EmailField(max_length=254)
   password = models.CharField(max_length=12)
   # last_login = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.username
