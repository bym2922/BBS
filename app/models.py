from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey("Author",max_length=100,on_delete=models.CASCADE)
    content = models.CharField(max_length=1500)
    # summary = models.CharField(max_length=300)


class Author(models.Model):
    name = models.CharField(max_length=30)
    pswd = models.CharField(max_length=50)
    art_nums = models.IntegerField()