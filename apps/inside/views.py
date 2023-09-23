from django.shortcuts import render
from apps.inside.models import Inside

def inside(request, id):
    inside = Inside.objects.get(id=id)
    context = {
        'inside': inside,
    }
    return render(request, "portfolio-singl.html", context)
