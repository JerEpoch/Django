from django import template
from amiibo.models import Amiibo
from django.db.models import  Sum

register = template.Library()



@register.assignment_tag
def get_grandTotal():
    return Amiibo.objects.aggregate(test_total1=Sum('price'))
