from django.urls import path
from .views import dashboard, edit_task, index, task_details, task_list, task_create, task_delete, user_login, user_logout, user_register

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', user_register, name='user_register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', task_create, name='task_create'),
    path('tasks/edit/<int:pk>/', edit_task, name='edit_task'),  # Add this path
    path('tasks/delete/<int:pk>/', task_delete, name='task_delete'),
    path('tasks/details/<int:pk>/', task_details, name='task_details'),
]