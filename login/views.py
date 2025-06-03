from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpRequest

def group_check(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect('/')  # Redirect to homepage or login

    user_groups = Group.objects.filter(user=request.user)
    group = user_groups.first()

    if group:
        if group.name == "Student":
            return redirect('/student/')
        elif group.name == "Teacher":
            return redirect('/teacher/')

    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

class RegisterTeacherView(TemplateView):
    template_name = "register_teacher.html"

class RegisterStudentView(TemplateView):
    template_name = "register_student.html"
