from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:project_id>/', views.project, name='project'),
    path('add_project', views.add_project, name='add_project'),
    path('add_interval/<int:project_id>/', views.add_interval, name='add_interval'),
]