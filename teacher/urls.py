from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher, name='teacher_home'),
    path('my_appointment/', views.teacher, name='teacher_appointment'),
    path('create_appointment/', views.teacher_appointment_list, name='teacher_appointment_list'),
    path('create_appointment/delete/<int:id>/', views.appointment_delete, name='appointment_delete'),
    path('create_appointment/update/<int:id>/', views.teacher_appointment_update, name='teacher_appointment_update'),
]
