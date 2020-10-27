from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.views.generic import DetailView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.urls import reverse
# Create your views here.

def index(request):
	projects = Project.objects.all()
	print("projects: ", projects)
	form = ProjectForm()
	
	if request.method == 'POST':
		form = ProjectForm(request.POST)

		if form.is_valid():
			form.save()
		else:
			print(form.errors)
		return redirect('/')

	context = {'projects': projects, 'form': form}
	return render(request, 'projects/list_project.html', context)

class ProjectDetailView(DetailView):
    model = Project

def updateProject(request, pk):
	project_inst = Project.objects.get(id=pk)

	form = ProjectForm(instance=project_inst)

	if request.method == 'POST':
		form = ProjectForm(request.POST, instance=project_inst)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form': form}
	return render(request, 'projects/update_project.html', context)


def deleteProject(request, pk):
	item = Project.objects.get(id=pk)
	if request.method == 'POST':
		item.delete()
		return redirect('/')
	context = {'item': item}
	return render(request, 'projects/delete_project.html', context)
	

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['GET'])
def taskListView(request):
	tasks = Task.objects.all()
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetailView(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(task, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskUpdateView(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
def taskDeleteView(request, pk):
	task = Task.objects.get(id=pk)
	primary_key = task.project.pk
	task.delete()
	return redirect('project_detail', pk=primary_key)