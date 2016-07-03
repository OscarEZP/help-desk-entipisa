from __future__ import unicode_literals

from django.db import models

class Department(models.Model):
	name = models.CharField(max_length=100, verbose_name='Nombre')
	descripcion = models.TextField(max_length=200, verbose_name='Descripcion')


	def __unicode__(self):
		return self.name