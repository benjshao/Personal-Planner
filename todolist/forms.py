from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    category = forms.ChoiceField(choices = category_choices, label="", initial='', widget=forms.Select(), required=True)
    due_date = forms.CharField(label='search',widget=forms.TextInput(attrs={'placeholder':'Due Date: yyyy-mm-dd'}))
    class Meta:
        model = Task
        fields = '__all__'