from django import forms
from .models import *



class OrderForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
