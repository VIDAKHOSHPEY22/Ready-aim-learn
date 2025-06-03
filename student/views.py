from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group
from teacher.models import Appointment

def quick_appointment(request):
    group = Group.objects.filter(user=request.user).first()
    group_name = group.name if group else None
    
    if group_name == "Student":
        user_name = request.user.get_username()
        appointment_list = Appointment.objects.all().order_by("-user")
        
        q = request.GET.get("q")
        if q:
            appointment_list = appointment_list.filter(user__first_name__icontains=q)
        
        context = {
            "query": appointment_list,
            "user_name": user_name,
        }
        return render(request, 'student_quick_appointment.html', context)
    
    return redirect('home')  # Replace 'home' with your actual homepage url name


def student(request):
    group = Group.objects.filter(user=request.user).first()
    group_name = group.name if group else None
    
    if group_name == "Student":
        user_name = request.user.get_username()
        appointment_list = Appointment.objects.filter(appointment_with=user_name).order_by("-id")
        
        q = request.GET.get("q")
        if q:
            appointment_list = appointment_list.filter(user__first_name__icontains=q)
        
        context = {
            "query": appointment_list,
            "user_name": user_name,
        }
        return render(request, 'student.html', context)
    
    return redirect('home')


def appointment_book(request, id):
    group = Group.objects.filter(user=request.user).first()
    group_name = group.name if group else None
    
    if group_name == "Student":
        user_name = request.user.get_username()
        appointment = get_object_or_404(Appointment, id=id)
        
        appointment.appointment_with = user_name
        appointment.save()
        
        return redirect('student')  # Use your named URL pattern here
    
    return redirect('home')
