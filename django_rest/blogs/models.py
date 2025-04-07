from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id = models.CharField(max_length=50, null=True)
    blog_title = models.CharField(max_length=50)
    blog_body =models.TextField()

    def __str__(self):
        return self.blog_title
    
class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments') # using foreignKey to make some relation between blogs model and comments model
    comment = models.TextField()

    def __str__(self):
        return self.comment