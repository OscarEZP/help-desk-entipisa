from django.contrib import admin

from .models import *


class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('Afectados', 'description', 'solventado', 'inicio', 'fin',)

admin.site.register(Requerimientos, RequirementsAdmin)
