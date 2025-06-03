from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='index.html'), name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('group/', views.group_check, name='group'),
    path('register_teacher/', views.RegisterTeacherView.as_view(), name='register_teacher'),
    path('register_student/', views.RegisterStudentView.as_view(), name='register_student'),
]
