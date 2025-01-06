from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to="pics")
    desc=models.CharField(max_length=500 , null=True)
    def __str__(self):
        return self.title

