from django.urls import path
from .views import task_list, add_task, delete_task, mark_completed

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('mark_completed/<int:pk>/', mark_completed, name='mark_completed'),
]
