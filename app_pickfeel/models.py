from django.db import models

# Create your models here.


class Category1(models.Model):
    title = models.CharField(max_length=30)


class Category2(models.Model):
    title = models.CharField(max_length=30)


class Category3(models.Model):
    title = models.CharField(max_length=30)