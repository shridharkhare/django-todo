from django.urls import path
from . import views


app_name = 'tasks'


urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>/', views.edit_task, name='edit'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
    path('toggle/<int:pk>/', views.toggle_complete, name='toggle'),
]
