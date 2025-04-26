from django.urls import path
from .views import Tasklist,TaskDetail,TaskCreate,TaskUpdate,TaskDeleteView,CustomLoginView,RegisterPage,custom_logout

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',custom_logout,name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('',Tasklist.as_view(),name='tasks'),
    path('task/<int:pk>',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>',TaskDeleteView.as_view(),name='task-delete'),

]
