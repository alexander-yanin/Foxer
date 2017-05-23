from django.db import models
from authsys.models import User
from picture.models import Picture


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User)
    picture = models.ManyToManyField(Picture)

    def __str__(self):
        return self.user.login


class Payment(models.Model):
    user = models.ForeignKey(User)
    picture = models.ManyToManyField(Picture, blank=True)
    cost = models.FloatField()

    def __str__(self):
        return self.user.login
