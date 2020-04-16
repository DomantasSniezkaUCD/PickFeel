from django.urls import path
from app_pickfeel import views

urlpatterns = [
    path('', views.pickfeelhome, name='pick-feel-home'),
    path('refresh/', views.pickfeelhome, name='pick-feel-home'),

]