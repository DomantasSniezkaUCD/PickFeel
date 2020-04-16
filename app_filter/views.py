from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ImageForm, ImageForm_Normal
from .models import Image


def pickfeel_filter_normal(request):
    # obj = get_object_or_404(Image)
    form = ImageForm_Normal(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "app_filter/filter-normal.html", context)



def pickfeel_filter_mania(request):
    return render(request, "app_filter/filter-mania.html")

def pickfeel_filter_depression(request):
    return render(request, "app_filter/filter-depression.html")

