from django.urls import path
from . import views

urlpatterns = [
    path('normal/', views.pickfeel_filter_normal, name='pick-feel-filter-normal'),
    path('mania/', views.pickfeel_filter_mania, name='pick-feel-filter-mania'),
    path('depression/', views.pickfeel_filter_depression, name='pick-feel-filter-depression'),
]