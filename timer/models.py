from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.name

class Interval(models.Model):
    project = models.ForeignKey(Project, null=False, blank=False, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.description