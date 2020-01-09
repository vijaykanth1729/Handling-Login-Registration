from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        context = {'user_name':request.user}
        return render(request, 'home.html' , context)
    else:
        return render(request, 'home.html', {'user_name':request.user})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'index.html', {})

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = User.objects.create_user(username=name, email=email, password=password1)
        user.save()
        return redirect('/login/')
    else:
        return render(request, 'register.html', {})

def form_addition(request):
    return render(request, 'form.html', {})

def result(request):
    try:
        a = request.POST['n1']
        x = int(a)
        b = request.POST['n2']
        y = int(b)
        z = x+y
        return HttpResponse(f"Sum of two numbers is: {z}")
    except ValueError:
        return HttpResponse("No valid input")




