from django.shortcuts import render
from projects.models import Project

def project_index(request):
    # perform query to the projects table
    projects = Project.objects.all()
    # creating a dictionary with projects
    # used to send information to the view
    context = {
        'projects': projects
    }
    # render that has context as an argument
    return render(request, 'project_index.html', context)

# method that will return the project detail page
def project_detail(request, pk):
    # query to the projects table that will return the project with
    # primary key pk
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)