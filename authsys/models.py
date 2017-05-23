from django.db import models


# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return self.login
