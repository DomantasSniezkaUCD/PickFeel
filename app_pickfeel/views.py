from django.shortcuts import render
from django.http import HttpResponse
from app_pickfeel.templatetags import random_Image
from .models import emotionSelected
import datetime
from django.contrib.auth.decorators import login_required


@login_required
def pickfeelhome(request):
    context = {}
    return render(request, 'app_pickfeel/pickfeel.html', context)


@login_required
def refresh_button(request):

    if request.GET.get('refresh-btn'):
        return render(request, 'app_pickfeel/pickfeel.html')


def addition(request):
	if request.method == 'POST' and request.user.is_authenticated:
		emotion_picked = "none"
		for name in request.POST.getlist('checked-radio'):
			emotion_picked = name
		emotion = emotionSelected(user=request.user, emotion=emotion_picked, time=datetime.datetime.now())
		emotion.save()
	return render(request, 'app_pickfeel/pickfeel.html')