from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('create_task', views.create_task,name='create_taskss'),
    path('view_tasks', views.view_tasks,name='view_tasks'),
]