from django.urls import path
from . import views

from .views import (
    student,
    quick_appointment,
    appointment_book,
)

urlpatterns = [
    path('', student, name='student'),
    path('my_appointment/', student, name='student'),
    path('quick_appointment/', quick_appointment, name='quick_appointment'),
    path('update/<int:id>/', appointment_book, name='appointment_update'),
]
