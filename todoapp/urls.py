from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.index, name='project_list_view'),
	path('update_project/<str:pk>/', views.updateProject, name='update_project'),
	path('delete_project/<str:pk>/', views.deleteProject, name='delete_project'),
	path('project_detail/<str:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
	path('task_create/', views.TaskCreateView.as_view(), name='task_create'),
	path('project_detail/<str:project_pk>/task_detail/<str:pk>', views.TaskDetailView.as_view(), name='task_detail'), 
	path('task_update/<str:pk>', views.TaskUpdateView.as_view(), name='task_update'),
	path('task_delete/<str:pk>', views.TaskDeleteView.as_view(), name='task_delete'), 
]
# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += staticfiles_urlpatterns()