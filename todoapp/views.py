from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User


def index(request):
    projects = Project.objects.all()
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('/')

    context = {'projects': projects, 'form': form}
    return render(request, 'todoapp/list_project.html', context)


class ProjectDetailView(DetailView):
    model = Project


def updateProject(request, pk):
    project_inst = Project.objects.get(id=pk)
    form = ProjectForm(instance=project_inst)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project_inst)
        img = request.FILES.get('image', None)
        project_inst.image = img
        if form.is_valid():
            form.save()
            project_inst.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'todoapp/update_project.html', context)


def deleteProject(request, pk):
    item = Project.objects.get(id=pk)
    if request.method == 'POST':
        item.tasks.all().delete()
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'todoapp/delete_project.html', context)
    

class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    success_url ="/"

class TaskDetailView(DetailView):  
    model = Task 
    fields = [ 
        "assigned_to", 
        "reporter",
        "title",
        "description",
        "current_status"
    ]


class TaskUpdateView(UpdateView):  
    model = Task 
    fields = [ 
        "assigned_to", 
        "reporter",
        "title",
        "description",
        "current_status"
    ] 
    def get_success_url(self):
        project = self.object.project
        print(project.id)
        return reverse_lazy('project_detail', kwargs={'pk': project.id})


class TaskDeleteView(DeleteView): 
    model = Task 
    def get_success_url(self):
        project = self.object.project
        print(project.id)
        return reverse_lazy('project_detail', kwargs={'pk': project.id})

