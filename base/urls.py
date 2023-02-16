from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteTask, UserLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', TaskList.as_view(), name = "tasks"),

    path('task/<int:pk>', TaskDetail.as_view(), name = 'task'),

    #CRUD OPERATIONS
    path('task-create/', TaskCreate.as_view(), name = 'task-create' ),
    path('task-edit/<int:pk>/', TaskUpdate.as_view(), name = 'task-edit'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name = "task-delete"),

    #LOGIN,LOGOGUT & REGISTER
    path('user-login/', UserLoginView.as_view(), name = "user-login"),
    path('user-logout/', LogoutView.as_view(next_page = 'user-login'), name = 'user-logout'),
    path('register/', RegisterPage.as_view(), name = 'register'),


]