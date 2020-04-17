from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category1(models.Model):
    title = models.CharField(max_length=30)


class Category2(models.Model):
    title = models.CharField(max_length=30)


class Category3(models.Model):
    title = models.CharField(max_length=30)