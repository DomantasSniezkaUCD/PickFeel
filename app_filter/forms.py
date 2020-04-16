from django import forms
from .models import Image, Image_Normal


class ImageForm(forms.ModelForm):

    title = forms.CharField()

    class Meta:
        model = Image
        fields = {
            'title'
        }

class ImageForm_Normal(forms.ModelForm):

    title = forms.CharField()

    class Meta:
        model = Image_Normal
        fields = {
            'title'
        }