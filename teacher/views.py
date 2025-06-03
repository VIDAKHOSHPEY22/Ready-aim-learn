from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
from django.contrib.auth.models import Group


def teacher(request):
    # Check if logged-in user is a Teacher
    group_qs = Group.objects.filter(user=request.user)
    if not group_qs.exists():
        return redirect('http://127.0.0.1:8000/')
    group_name = str(group_qs[0])

    if group_name == "Teacher":
        user_name = request.user.get_username()
        appointment_list = Appointment.objects.filter(user=request.user).order_by("-id")

        q = request.GET.get("q")
        if q:
            appointment_list = appointment_list.filter(appointment_with__icontains=q)

        context = {
            "query": appointment_list,
            "user_name": user_name
        }
        return render(request, 'teacher.html', context)

    return redirect('http://127.0.0.1:8000/')


def teacher_appointment_list(request):
    group_qs = Group.objects.filter(user=request.user)
    if not group_qs.exists():
        return redirect('http://127.0.0.1:8000/')
    group_name = str(group_qs[0])

    if group_name == "Teacher":
        user_name = request.user.get_username()
        appointment_list = Appointment.objects.filter(user=request.user).order_by("-id")

        q = request.GET.get("q")
        if q:
            appointment_list = appointment_list.filter(date__icontains=q)

        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            new_appointment = form.save(commit=False)
            new_appointment.user = request.user
            new_appointment.save()
            messages.success(request, 'Post Created Successfully')
            return redirect('teacher_appointment_list')  # better to redirect after POST

        context = {
            "query": appointment_list,
            "user_name": user_name,
            "form": form,
        }
        return render(request, 'teacher_create_appointment.html', context)

    return redirect('http://127.0.0.1:8000/')


def appointment_delete(request, id):
    group_qs = Group.objects.filter(user=request.user)
    if not group_qs.exists():
        return redirect('http://127.0.0.1:8000/')
    group_name = str(group_qs[0])

    if group_name == "Teacher":
        appointment = get_object_or_404(Appointment, id=id, user=request.user)
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully.')
        return redirect('teacher_appointment_list')

    return redirect('http://127.0.0.1:8000/')


def teacher_appointment_update(request, id):
    group_qs = Group.objects.filter(user=request.user)
    if not group_qs.exists():
        return redirect('http://127.0.0.1:8000/')
    group_name = str(group_qs[0])

    if group_name == "Teacher":
        appointment = get_object_or_404(Appointment, id=id, user=request.user)

        form = AppointmentForm(request.POST or None, instance=appointment)
        if form.is_valid():
            updated_appointment = form.save(commit=False)
            updated_appointment.user = request.user
            updated_appointment.save()
            messages.success(request, 'Appointment updated successfully.')
            return redirect('teacher_appointment_list')

        appointment_list = Appointment.objects.filter(user=request.user).order_by("-id")
        q = request.GET.get("q")
        if q:
            appointment_list = appointment_list.filter(date__icontains=q)

        context = {
            "query": appointment_list,
            "user_name": request.user.get_username(),
            "form": form,
        }
        return render(request, 'teacher_appointment_update.html', context)

    return redirect('http://127.0.0.1:8000/')
