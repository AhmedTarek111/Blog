from django import forms
from .models import Post,Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class Postform(forms.ModelForm):
    class Meta:
        model= Post
        exclude =('author',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ['comment']
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

