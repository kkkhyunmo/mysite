from django.shortcuts import render, redirect
from .models import Info
from django.core.exceptions import ObjectDoesNotExist

def laviniaA(request):
    title = 'laviniaA'
    contents = {
        'title' : title,
    }
    return render(request, "eventpage/index.html", contents)

def laviniaA_false(request, webtoon):
    title = 'laviniaA'
    contents = {
        'title' : title,
        'webtoon' : webtoon,
    }
    return render(request, "eventpage/index.html", contents)

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
    contents = {
        'title' : title,
    }
    return render(request, "eventpage/index.html", contents)

def laviniaN_false(request, webtoon):
    title = 'laviniaN'
    contents = {
        'title' : title,
        'webtoon' : webtoon,
    }
    return render(request, "eventpage/index.html", contents)

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
    contents = {
        'title' : title,
    }
    return render(request, "eventpage/index.html", contents)

def rainbowhouseA_false(request, webtoon):
    title = 'rainbowhouseA'
    contents = {
        'title' : title,
        'webtoon' : webtoon,
    }
    return render(request, "eventpage/index.html", contents)

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
    contents = {
        'title' : title,
    }
    return render(request, "eventpage/index.html", contents)

def rainbowhouseN_false(request, webtoon):
    title = 'rainbowhouseN'
    contents = {
        'title' : title,
        'webtoon' : webtoon,
    }
    return render(request, "eventpage/index.html", contents)

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