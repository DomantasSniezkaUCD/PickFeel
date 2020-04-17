from django.urls import path
from app_register import views

urlpatterns = [
    path('', views.register, name='register'),

]


#     path('register/', views.register, name='register'),