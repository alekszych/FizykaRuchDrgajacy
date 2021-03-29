from django.shortcuts import render
import requests
import shutil

# Create your views here.

apiIp = "http://65.21.61.66:3000/"


def home(request):
    return render(request, 'home_page.html', {

    })


def vChart(request):
    if request.POST is not None:
        if ("amplituda" in request.POST
                and "okres_drgan" in request.POST
                and "faza" in request.POST):
            if float(request.POST["amplituda"]) > 0 and float(request.POST["faza"]) > 0 and float(request.POST["okres_drgan"]) > 0:
                response = str(apiIp + "wykres_v?" + "amp=" + request.POST["amplituda"] + "&" + "okres=" + request.POST[
                    "okres_drgan"] + "&" + "faza=" + request.POST["faza"])
                return render(request, 'vChart_page.html', {
                    "chart": response,
                })
            else:
                return render(request, 'vChart_page.html', {
                    "error": True,
                })
    return render(request, 'vChart_page.html', {})


def xChart(request):
    if request.POST is not None:
        if ("amplituda" in request.POST and "okres_drgan" in request.POST):
            if float(request.POST["amplituda"]) > 0 and float(request.POST["okres_drgan"]) > 0:
                response = str(
                    apiIp + "wykres_x?" + "amp=" + request.POST["amplituda"] + "&" + "okres=" + request.POST["okres_drgan"])
                return render(request, 'xChart_page.html', {
                    "chart": response,
                })
            else:
                return render(request, 'xChart_page.html', {
                    "error": True,
                })
    return render(request, 'xChart_page.html', {})


def aChart(request):
    if request.POST is not None:
        if ("amplituda" in request.POST
                and "okres_drgan" in request.POST
                and "faza" in request.POST):
            if float(request.POST["amplituda"]) > 0 and float(request.POST["okres_drgan"]) > 0 and float(request.POST["faza"]) > 0:
                response = str(apiIp + "wykres_a?" + "amp=" + request.POST["amplituda"] + "&" + "okres=" + request.POST[
                    "okres_drgan"] + "&" + "faza=" + request.POST["faza"])
                return render(request, 'aChart_page.html', {
                    "chart": response,
                })
            else:
                return render(request, 'aChart_page.html', {
                    "error": True,
                })
    return render(request, 'aChart_page.html', {})


def tValues(request):
    if request.POST is not None:
        if ("amplituda" in request.POST
                and "okres_drgan" in request.POST
                and "faza" in request.POST
                and "czas" in request.POST):
            if request.POST["amplituda"] is not None and float(request.POST["okres_drgan"]) is not None and float(request.POST["czas"]) is not None:
                if float(request.POST["amplituda"]) > 0 and float(request.POST["okres_drgan"]) > 0 and float(request.POST["czas"]) > 0:
                    response = requests.get(
                        apiIp + "wartosci_t?" + "amp=" + request.POST["amplituda"] + "&" + "okres=" + request.POST[
                            "okres_drgan"] + "&" + "faza=" + request.POST["faza"] + "&" + "czas=" + request.POST["czas"])
                    if response.status_code == 200:
                        return render(request, 'tValues_page.html', {
                            "x": response.json()["x(t)"],
                            "v": response.json()["v(t)"],
                            "a": response.json()["a(t)"]
                        })
                    else:
                        print("blad serwera")
                else:
                    return render(request, 'tValues_page.html', {
                        "error": True,
                    })
            else:
                return render(request, 'tValues_page.html', {
                    "error": True,
                })
    return render(request, 'tValues_page.html', {})


def pendulum(request):
    if request.POST is not None:
        if "amplituda" in request.POST and "okres_drgan" in request.POST:
            if 0 < float(request.POST["amplituda"]) <= 7 and float(request.POST["okres_drgan"]) > 0:
                response = str(apiIp + "wahadlo?" + "amp=" + request.POST["amplituda"] + "&" + "okres=" + request.POST[
                    "okres_drgan"])
                return render(request, 'pendulum_page.html', {
                    "gif": response,
                })
            else:
                return render(request, 'pendulum_page.html', {
                    "error": True,
                })

    return render(request, 'pendulum_page.html', {})
