from django.shortcuts import render, redirect

from .models import Project
from django.contrib.auth.models import User

def index(request):

    """ view returns trata app home """

    projects = None

    if request.user.is_authenticated: 
        projects = Project.objects.filter(user=request.user)

    context = {
        'projects': projects
    }

    return render(request, 'timer/index.html', context)


def add_project(request):

    """ view creates new project """ 

    if request.POST:
        project = Project(user=request.user, name=request.POST['projectName'])
        project.save()
    
    return redirect('index')

