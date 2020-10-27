from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

# Create your models here.

def upload_project_image(instance, filename):
    return "todoapp/files/{filename}".format(filename=filename)

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_project_image, null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("project_detail",kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title

class Task(models.Model):
    STATUS= (
        ('New', 'New'),
        ('Assigned', 'Assigned'),
        ('Selected For Development', 'Selected For Development'),
        ('In Progress', 'In Progress'),
        ('Blocked', 'Blocked'),
        ('Completed', 'Completed'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    current_status = models.CharField(max_length=50, choices=STATUS, default='New')

    def get_absolute_url(self):
        return reverse("project_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
