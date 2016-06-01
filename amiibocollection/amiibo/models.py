from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Amiibo(models.Model):

    name = models.CharField(max_length=255)
    series = models.CharField(max_length=255)

    owner = models.ForeignKey('auth.User')
    #owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=)
    #owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):

        return ' '.join([self.name, self.series])

    def get_absolute_url(self):

        return reverse('amiibo-view', kwargs={'pk': self.id})
