from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def home(request):
    return render(request, 'home.html')


@login_required
def projects(request):
    search = request.GET.get('search')
    department = Department.objects.all()
    if search:
        p = Project.objects.filter(name__icontains=search)
    else:
        p = Project.objects.all()
    paginator = Paginator(p, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    return render(request, 'projects.html', {'searchTerm': search, 'projects': project, 'departments': department})


@login_required
def sorted(request, department_id):
    search = request.GET.get('search')
    department = Department.objects.all()
    if search:
        p = Project.objects.filter(name__icontains=search)
    else:
        p = Project.objects.all()
    paginator = Paginator(p, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    departmentId = get_object_or_404(Department, pk=department_id)
    project = Project.objects.filter(department=departmentId)
    return render(request, 'projects.html', {'searchTerm': search, 'projects': project, 'departments': department})


@login_required
def add_project(request):
    if request.method == 'POST':
        supervisor = Supervisor.objects.get(id=1)
        department = Department.objects.get(name=request.POST['department'])
        project = Project(name=request.POST['name'], student=request.POST['student'],
                          department=department, supervisor=supervisor, document=request.POST['document'])
        project.save()
        return redirect('projects')
    else:
        department = Department.objects.all()
        return render(request, 'add_project.html', {'departments': department})


@login_required
def add_staff(request):
    if request.method == 'GET':
        return render(request, 'add_staff.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                staff = User.objects.create_user(request.POST['username'], request.POST['email'],
                                                 password=request.POST['password1'])
                staff.save()
                return redirect('projects')
            except IntegrityError:
                return render(request, 'add_staff.html', {'error': 'Username already taken. Choose new username.'})
        else:
            return render(request, 'add_staff.html', {'error': 'password does not match!'})


def admin(request):
    return render(request, 'admin.html')
