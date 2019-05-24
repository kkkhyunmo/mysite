from django.shortcuts import render, redirect
from .models import Info
from django.core.exceptions import ObjectDoesNotExist
import urllib.request

def laviniaA(request):
    ip = urllib.request.urlopen('https://api.ipify.org/').read().decode()
    print(ip)
    title = 'laviniaA'
    context = {
        'title' : title,
        'ip' : ip,
    }
    return render(request, "eventpage/index.html", context)

def laviniaA_false(request, webtoon):
    title = 'laviniaA'
    context = {
        'title' : title,
        'webtoon' : webtoon,
    }
    return render(request, "eventpage/index.html", context)

def laviniaA_success(request):
    if request.method == 'POST':
        try:
            webtoon = Info.objects.get(webtoon=request.POST['webtoon']).webtoon
            if webtoon:
                return redirect('laviniaA_false', webtoon=webtoon)
        except ObjectDoesNotExist:
            Info.objects.create(webtoon=request.POST['webtoon'],
                                name=request.POST['name'],
                                phone=request.POST['phone'],
                                )
    return render(request, "eventpage/success.html")

def laviniaN(request):
    title = 'laviniaN'
    context = {
        'title' : title,
    }
    return render(request, "eventpage/index.html", context)

def laviniaN_false(request, webtoon):
    title = 'laviniaN'
    context = {
        'title' : title,
        'webtoon' : webtoon,
    }
    return render(request, "eventpage/index.html", context)

def laviniaN_success(request):
    if request.method == 'POST':
        try:
            webtoon = Info.objects.get(webtoon=request.POST['webtoon']).webtoon
            if webtoon:
                return redirect('laviniaN_false', webtoon=webtoon)
        except ObjectDoesNotExist:
            Info.objects.create(webtoon=request.POST['webtoon'],
                                name=request.POST['name'],
                                phone=request.POST['phone'],
                                )
    return render(request, "eventpage/success.html")

def rainbowhouseA(request):
    title = 'rainbowhouseA'
    context = {
        'title' : title,
    }
    return render(request, "eventpage/index.html", context)

def rainbowhouseA_false(request, webtoon):
    title = 'rainbowhouseA'
    context = {
        'title' : title,
        'webtoon' : webtoon,
    }
    return render(request, "eventpage/index.html", context)

def rainbowhouseA_success(request):
    if request.method == 'POST':
        try:
            webtoon = Info.objects.get(webtoon=request.POST['webtoon']).webtoon
            if webtoon:
                return redirect('rainbowhouseA_false', webtoon=webtoon)
        except ObjectDoesNotExist:
            Info.objects.create(webtoon=request.POST['webtoon'],
                                name=request.POST['name'],
                                phone=request.POST['phone'],
                                )
    return render(request, "eventpage/success.html")

def rainbowhouseN(request):
    title = 'rainbowhouseN'
    context = {
        'title' : title,
    }
    return render(request, "eventpage/index.html", context)

def rainbowhouseN_false(request, webtoon):
    title = 'rainbowhouseN'
    context = {
        'title' : title,
        'webtoon' : webtoon,
    }
    return render(request, "eventpage/index.html", context)

def rainbowhouseN_success(request):
    if request.method == 'POST':
        try:
            webtoon = Info.objects.get(webtoon=request.POST['webtoon']).webtoon
            if webtoon:
                return redirect('rainbowhouseN_false', webtoon=webtoon)
        except ObjectDoesNotExist:
            Info.objects.create(webtoon=request.POST['webtoon'],
                                name=request.POST['name'],
                                phone=request.POST['phone'],
                                )
    return render(request, "eventpage/success.html")