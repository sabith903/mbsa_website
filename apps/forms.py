from django import forms
from .models import Image

class imagesForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']
