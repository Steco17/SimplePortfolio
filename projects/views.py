from django.shortcuts import render

from django.http import HttpResponse

from .models import Projects

# Create your views here.

def index(request):
    projects = Projects.objects
    return render(request, 'projects/index.html', {'projects':projects})


