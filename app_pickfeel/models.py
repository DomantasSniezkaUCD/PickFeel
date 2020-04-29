from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class emotionSelected(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=50)
    time = models.DateTimeField()

    def __str__(self):
        return "Username:" + self.user.username + " emotion:" + self.emotion

    class Meta:
        verbose_name = "Selected Emotions"
        verbose_name_plural = "Selected Emotions"
