from django.shortcuts import render, redirect, get_object_or_404

from .models import Project, Interval
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

def project(request, project_id):

    """ view returns details specific project """
    
    project = get_object_or_404(Project, pk=project_id)
    intervals = Interval.objects.filter(project=project_id)
    print(intervals)
    context = {
        'project': project,
        'intervals': intervals
    }
    
    return render(request, 'timer/project_detail.html', context)

def add_project(request):

    """ view creates new project """ 

    if request.POST:
        project = Project(user=request.user, name=request.POST['projectName'])
        project.save()
    
    return redirect('index')