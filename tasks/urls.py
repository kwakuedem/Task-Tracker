from django.urls import path
from .views import task_list, task_create, task_edit, task_delete, user_login, user_logout, user_register

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', user_register, name='user_register'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', task_create, name='task_create'),
    path('tasks/edit/<int:pk>/', task_edit, name='task_edit'),
    path('tasks/delete/<int:pk>/', task_delete, name='task_delete'),
]