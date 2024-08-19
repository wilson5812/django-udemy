from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

"""
Hardcoded Data prior to Database setup
projects_list = [
    {
        'id':'1',
        'title':'Ecommerce Website',
        'description':'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title':'Portfolio Website',
        'description':'Developer Portfolio Website',
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'open source social media project',
    },
]
"""
def projects(request):
    # Original
        # return HttpResponse('Here are our products')
        # msg = 'This is the Projects Page view'
        # context = {'message':msg, 'projects':projects_list}
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, primary_key):
    # Original
    # return HttpResponse(f'Single Project id number: {primary_key}')
    # project_object = None
    # for project_passed in projectslist:
    #    if project_passed['id'] == primary_key:
    #        project_object = project_passed
    project_object = Project.objects.get(id=primary_key)
    tags = project_object.tags.all()
    context = {'project': project_object, 'tags': tags}
    return render(request, 'projects/single_project.html', context)


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = { 'form': form }
    return render(request, 'projects/project_form.html', context)

def update_project(request, primary_key):

    project_selected = Project.objects.get(id=primary_key)
    form = ProjectForm(instance=project_selected)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project_selected)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = { 'form': form }
    return render(request, 'projects/project_form.html', context)

def delete_project(request, primary_key):

    project_deleted = Project.objects.get(id=primary_key)
    if request.method == 'POST':
        project_deleted.delete()
        return redirect('projects')

    context = { 'object': project_deleted }
    return render(request, 'projects/delete_template.html', context)