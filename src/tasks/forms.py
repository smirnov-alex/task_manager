from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('title', 'description')
