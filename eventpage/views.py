from django.shortcuts import render, redirect
from .models import dbinfo
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

def validate_username(request):
    username = request.GET.get('username', None)

    res = dbinfo.objects.filter(name=username).exists()
    is_taken = True
    if res:
        is_taken = False

    data = {
        'is_taken': is_taken
    }
    return JsonResponse(data)

def validate_userphone(request):
    userphone = request.GET.get('userphone', None)

    res = dbinfo.objects.filter(phone=userphone).exists()
    as_taken = True
    if res:
        as_taken = False
    data = {
        'as_taken': as_taken
    }
    return JsonResponse(data)

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
        try:
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
        try:
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
        try:
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
        try:
            dbinfo.objects.create(name=request.POST['name'], phone=request.POST['phone'])
        except ObjectDoesNotExist:
            pass
        return render(request, "eventpage/success.html")