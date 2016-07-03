from __future__ import unicode_literals

from django.db import models
from falla.models import Falla
from departamento.models import Department
from django.contrib.auth.models import User


class Requerimientos(models.Model):
    Afectados = models.IntegerField(default=0, verbose_name="Usuarios afectados")
    user = models.ForeignKey(User, verbose_name="Asignado a")
    falla = models.ForeignKey(Falla, verbose_name='Tipo de Falla')
    description = models.TextField(max_length=200, verbose_name="Descripcion de la falla")
    department = models.ForeignKey(Department, verbose_name='Departmento')
    solventado = models.BooleanField(default=False)
    solucion = models.TextField(max_length=200, verbose_name="Describa la solucion", blank=True, null=True)
    report = models.CharField(max_length=100, verbose_name='Reportado a')
    inicio = models.DateTimeField(verbose_name='Fecha de inicio')
    fin = models.DateTimeField(verbose_name='Fecha fin')