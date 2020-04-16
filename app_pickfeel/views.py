from django.shortcuts import render
from django.http import HttpResponse
from app_pickfeel.templatetags import random_Image


def pickfeelhome(request):
    context = {}
    return render(request, 'app_pickfeel/pickfeel.html', context)


def refresh_button(request):

    if request.GET.get('refresh-btn'):
        return render(request, 'app_pickfeel/pickfeel.html')


