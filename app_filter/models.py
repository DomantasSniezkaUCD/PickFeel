from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=30)

class Image_Normal(models.Model):
    title = models.CharField(max_length=30)