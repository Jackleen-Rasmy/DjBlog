from .models import *
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['user', 'comment']
        