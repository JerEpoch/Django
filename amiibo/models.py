from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Sum

# Create your models here.

class Amiibo(models.Model):

    name = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    price = models.FloatField(max_length = 6, default=12.99)
    gtotals = models.FloatField(default=0)

    owner = models.ForeignKey('auth.User')
    #owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=)
    #owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def save(self, *args, **kwargs):
        self.total()

        super(Amiibo, self).save(*args, **kwargs)

    def total(self):
        gtotal=0
        gtotal = Amiibo.objects.aggregate(total_sum=Sum('price'))
        return gtotal['total_sum']
        #objects = Amiibo.objects.all()
        #totals = 0

        #for object in objects:
        #    totals += object.price

    #    self.total = totals


    def get_price(self):
        return self.price


    def __str__(self):

        return ' '.join([self.name, self.series])

    def get_absolute_url(self):

        return reverse('amiibo-view', kwargs={'pk': self.id})
