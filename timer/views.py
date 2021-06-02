from django.shortcuts import render, redirect

from .models import Project, Interval
from django.contrib.auth.models import User

def index(request):

    """ view returns trata app home """

    projects = None

    if request.user.is_authenticated: 
        projects = Project.objects.filter(user=request.user)

        # attach completed intervals to each project 
        for project in projects: 
            project.intervals = Interval.objects.filter(project=project.id)

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

