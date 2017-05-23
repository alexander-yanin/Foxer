from django.db import models
from authsys.models import User
from django.utils import timezone

import os


# Create your models here.
def get_upload_image(self, filename):
    return os.path.join('authors', self.user.login, filename)


class Picture(models.Model):
    user = models.ForeignKey(User)
    path = models.ImageField(upload_to=get_upload_image)
    name = models.CharField(max_length=100, blank=True)
    price = models.FloatField(default=0.0)
    sale_count = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s/%s' % (self.user.login, self.name)
