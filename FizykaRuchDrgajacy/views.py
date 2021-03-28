from django.shortcuts import render
import requests
import shutil

# Create your views here.

apiIp = "http://83.11.31.190:25565/"

def home(request):
    return render(request, 'home_page.html', {

    })


def vChart(request):
    if request.POST is not None:
        if ("amplituda" in request.POST
                and "okres_drgan" in request.POST
                and "faza" in request.POST):
            response = str(apiIp+"wykres_v?"+"amp="+request.POST["amplituda"]+"&"+"okres="+request.POST["okres_drgan"]+"&"+"faza="+request.POST["faza"])
            return render(request, 'vChart_page.html', {
                "chart": response,
            })
    return render(request, 'vChart_page.html', {})


def xChart(request):
    if request.POST is not None:
        if ("amplituda" in request.POST and "okres_drgan" in request.POST):
            response = str(apiIp+"wykres_x?"+"amp="+request.POST["amplituda"]+"&"+"okres="+request.POST["okres_drgan"])
            return render(request, 'xChart_page.html', {
                "chart": response,
            })
    return render(request, 'xChart_page.html', {})


def aChart(request):
    if request.POST is not None:
        if ("amplituda" in request.POST
                and "okres_drgan" in request.POST
                and "faza" in request.POST):
            response = str(apiIp+"wykres_a?"+"amp="+request.POST["amplituda"]+"&"+"okres="+request.POST["okres_drgan"]+"&"+"faza="+request.POST["faza"])
            return render(request, 'aChart_page.html', {
                "chart": response,
            })
    return render(request, 'aChart_page.html', {})


