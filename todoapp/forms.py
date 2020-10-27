from django import forms
from django.forms import ModelForm
from .models import Project, Task

class ProjectForm(forms.ModelForm):
	# project = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Add new Project'}))
	class Meta:
		model = Project
		fields = '__all__'


class TaskForm(forms.ModelForm):
	task = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Add new Task'}))
	class Meta:
		model = Task
		fields = '__all__'