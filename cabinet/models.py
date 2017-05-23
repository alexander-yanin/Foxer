from django.db import models
from authsys.models import User
from picture.models import Picture


# Create your models here.
class Sale(models.Model):
    user = models.OneToOneField(User)
    pictures = models.ManyToManyField(Picture)

    def __str__(self):
        return self.user.login
