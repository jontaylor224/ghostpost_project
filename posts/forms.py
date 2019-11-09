from django import forms
from .models import Post


class PostForm(forms.Form):
    content = forms.CharField(max_length=280, label='Make your post here')
    is_boast = forms.BooleanField(
        label='Check here to Boast! ', required=False)
