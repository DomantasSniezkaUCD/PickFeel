from django.urls import path
from . import views

urlpatterns = [
    path('', views.pickfeelinfo, name='pick-feel-info'),
]