from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('create_task', views.create_task,name='create_tasks'),
    path('view_tasks', views.view_tasks,name='view_tasks'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete_task/<str:pk>/', views.delete_task, name='delete_task'),

]