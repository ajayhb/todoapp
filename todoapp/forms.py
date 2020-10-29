from django import forms
from django.forms import ModelForm
from .models import Project, Task

class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            if field_name == 'title':
                field = self.fields.get(field_name)
                field.widget.attrs.update({'placeholder': 'Enter Project Title'})

class ProjectForm(PlaceholderMixin, forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'