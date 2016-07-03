from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import Requerimientos
from django.db.models import Count, Avg, Min, Max
import json
from django.http import HttpResponse

@staff_member_required
def metrics(request, *args, **kwargs):

    if kwargs['graph_type'] == "1":
        return get_metrics_requirements()

    if kwargs['graph_type'] == "2":
        return get_metrics_bug()

    if kwargs['graph_type'] == "3":
        return get_metrics_department()


def get_metrics_requirements(**kwargs):
    requirements = Requerimientos.objects.values('solventado').annotate(scount=Count('id'))

    data = []
    for requerimiento in requirements:
        if requerimiento['solventado'] == True:
            name = 'Soventado'
        else:
            name = 'No Soventado'

        data.append({'cant': requerimiento['scount'], 'name': name})

    return HttpResponse(json.dumps(data), content_type='application/json; utf-8')


def get_metrics_bug(**kwargs):
    requirements = Requerimientos.objects.values('falla__name').annotate(scount=Count('id'))
    data = []
    for requerimiento in requirements:
        data.append({'cant': requerimiento['scount'], 'name': requerimiento['falla__name']})

    return HttpResponse(json.dumps(data), content_type='application/json; utf-8')


def get_metrics_department(**kwargs):
    requirements = Requerimientos.objects.values('department__name').annotate(scount=Count('id'))
    data = []
    for requerimiento in requirements:
        data.append({'cant': requerimiento['scount'], 'name': requerimiento['department__name']})

    return HttpResponse(json.dumps(data), content_type='application/json; utf-8')