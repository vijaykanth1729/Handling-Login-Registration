from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product

def input(request):
    return render(request, 'input.html', {})

def insert(request):
    try:
        pid1 = int(request.GET['t1'])
        pname1 = request.GET['t2']
        pcost1 = float(request.GET['t3'])
        data_base = Product(pid=pid1, pname=pname1, pcost=pcost1)
        data_base.save()
        #return HttpResponse("<h2>Saved success!!</h2>")
        return redirect('db:display')
    except ValueError:
        return HttpResponse("<h2>Please submit the form with all the fields</h2>")


def display(request):
    data = Product.objects.all()
    context = {
        'records':data
    }

    return render(request, 'display.html', context)


