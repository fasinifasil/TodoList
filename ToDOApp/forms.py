from django import forms
from django.forms import ModelForm

from .models import *
class ToDoForm(forms.ModelForm):
    Title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Task'}))
    class Meta:
        model=ToDOList
        fields ='__all__'