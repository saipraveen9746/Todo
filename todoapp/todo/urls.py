


from django.urls import path
from .views import Taskcreate,RegisterPage,CustomLoginView,TaskList,Taskdetailview,TaskUpdate,TaskDelete
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('create/',Taskcreate.as_view(),name ='createtask'),
    path('register/',RegisterPage.as_view(),name = 'register'),
    path('',CustomLoginView.as_view(),name='login'),
    path('tasks/',TaskList.as_view(),name='task'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('task-details/<int:pk>/',Taskdetailview.as_view(),name='details'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='delete'),
    
]
