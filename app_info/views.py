from django.shortcuts import render
from django.http import HttpResponse


def pickfeelinfo(request):
    return render(request, 'app_info/info.html')

