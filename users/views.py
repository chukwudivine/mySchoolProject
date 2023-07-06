from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

            
def signin(request):
    if request.user.is_authenticated:
        return redirect(to='/projects')
    else:
        if request.method == 'GET':
            return render(request, 'login.html')
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('projects')
            else:
                return render(request, 'login.html', {'error': 'This user does not exist!'})


@login_required
def log_out(request):
    logout(request)
    return redirect('/')
