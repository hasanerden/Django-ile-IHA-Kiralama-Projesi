from django import forms
from .models import Airvehicles

class PostIHAForm(forms.ModelForm):
    class Meta:
        model = Airvehicles
        fields = [
            'brand',
            'model',
            'weight',
            'image',
            'description',
            'is_active',
            'category',
        ]