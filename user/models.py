from django.db import models

# Create your models here.

class User(models.Model):
    SEX = (
        ('F','男'),
        ('M','女'),
        ('U','保密'),
    )
    nickname = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    icon = models.ImageField()
    sex = models.CharField(max_length=8, choices=SEX)
    age = models.IntegerField()
