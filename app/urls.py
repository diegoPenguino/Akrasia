from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_task/', views.create_task, name='create_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('delete_re_task/<int:task_id>/', views.delete_repeating_task, name='delete_repeating_task'),
    path('mark_task/<int:task_id>/', views.mark_task, name='mark_task'),
]
