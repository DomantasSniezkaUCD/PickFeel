from django.shortcuts import render
from django.http import HttpResponse
from app_pickfeel.templatetags import random_Image
from django.contrib.auth.decorators import login_required


@login_required
def pickfeelhome(request):
    context = {}
    return render(request, 'app_pickfeel/pickfeel.html', context)

@login_required
def refresh_button(request):

    if request.GET.get('refresh-btn'):
        return render(request, 'app_pickfeel/pickfeel.html')


