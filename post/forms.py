from django import forms
from django.db.models import fields
from .models import Recruit

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['name','age','gender','body']
    
