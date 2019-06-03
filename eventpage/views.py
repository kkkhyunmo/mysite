from django.shortcuts import render, redirect
from .models import dbinfo
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


def index(request):
    return render(request, "eventpage/index1.html")

def laviniaA(request):
    title = 'laviniaA'
    context = {
        'title' : title,
    }
    return render(request, "eventpage/index.html", context)

def laviniaA_success(request):
    if request.method == 'POST':
        queryset = dbinfo.objects.all()
        name = queryset.filter(name=request.POST['name'])
        phone = queryset.filter(phone=request.POST['phone'])
        try:
            if name and phone:
                name = 'name'
                phone = 'phone'
                return render(request, "eventpage/index.html", {'name' : name, 'phone' : phone})
            elif name:
                name = 'name'
                return render(request, "eventpage/index.html", {'name': name })
            elif phone:
                phone = 'phone'
                return render(request, "eventpage/index.html", {'phone': phone})
            else:
                dbinfo.objects.create(name=request.POST['name'], phone=request.POST['phone'])

        except ObjectDoesNotExist:
            pass
        return render(request, "eventpage/success.html")

def laviniaN(request):
    title = 'laviniaN'
    context = {
        'title' : title,
    }
    return render(request, "eventpage/index.html", context)

def laviniaN_success(request):
    if request.method == 'POST':
        queryset = dbinfo.objects.all()
        name = queryset.filter(name=request.POST['name'])
        phone = queryset.filter(phone=request.POST['phone'])
        try:
            if name and phone:
                name = 'name'
                phone = 'phone'
                return render(request, "eventpage/index.html", {'name' : name, 'phone' : phone})
            elif name:
                name = 'name'
                return render(request, "eventpage/index.html", {'name': name })
            elif phone:
                phone = 'phone'
                return render(request, "eventpage/index.html", {'phone': phone})
            else:
                dbinfo.objects.create(name=request.POST['name'], phone=request.POST['phone'])

        except ObjectDoesNotExist:
            pass
        return render(request, "eventpage/success.html")

def rainbowhouseA(request):
    title = 'rainbowhouseA'
    context = {
        'title' : title,
    }
    return render(request, "eventpage/index.html", context)

def rainbowhouseA_success(request):
    if request.method == 'POST':
        queryset = dbinfo.objects.all()
        name = queryset.filter(name=request.POST['name'])
        phone = queryset.filter(phone=request.POST['phone'])
        try:
            if name and phone:
                name = 'name'
                phone = 'phone'
                return render(request, "eventpage/index.html", {'name' : name, 'phone' : phone})
            elif name:
                name = 'name'
                return render(request, "eventpage/index.html", {'name': name })
            elif phone:
                phone = 'phone'
                return render(request, "eventpage/index.html", {'phone': phone})
            else:
                dbinfo.objects.create(name=request.POST['name'], phone=request.POST['phone'])

        except ObjectDoesNotExist:
            pass
        return render(request, "eventpage/success.html")

def rainbowhouseN(request):
    title = 'rainbowhouseN'
    context = {
        'title' : title,
    }
    return render(request, "eventpage/index.html", context)

def rainbowhouseN_success(request):
    if request.method == 'POST':
        queryset = dbinfo.objects.all()
        name = queryset.filter(name=request.POST['name'])
        phone = queryset.filter(phone=request.POST['phone'])
        try:
            if name and phone:
                name = 'name'
                phone = 'phone'
                return render(request, "eventpage/index.html", {'name' : name, 'phone' : phone})
            elif name:
                name = 'name'
                return render(request, "eventpage/index.html", {'name': name })
            elif phone:
                phone = 'phone'
                return render(request, "eventpage/index.html", {'phone': phone})
            else:
                dbinfo.objects.create(name=request.POST['name'], phone=request.POST['phone'])

        except ObjectDoesNotExist:
            pass
        return render(request, "eventpage/success.html")