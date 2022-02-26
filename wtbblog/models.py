from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateField(blank=True,null=True)
    location=models.CharField(max_length=255)
    timetoread=models.CharField(max_length=255)
    image= models.CharField(max_length=255)
    post=models.TextField(blank=True)


    def __str__(self):
        return self.title
    