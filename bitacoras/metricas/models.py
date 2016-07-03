from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MetricasRequerimiento(models.Model):
    cant = models.IntegerField(default=0)