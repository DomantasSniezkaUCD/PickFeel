from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def pickfeelinfo(request):
    return render(request, 'app_info/info.html')

