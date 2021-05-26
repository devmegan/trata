from django.shortcuts import render

from .models import Project
from django.contrib.auth.models import User

def index(request):

    projects = None

    if request.user.is_authenticated: 
        projects = Project.objects.filter(user=request.user)

    context = {
        'projects': projects
    }

    return render(request, 'timer/index.html', context)