from django import forms
from .models import Comment


class Comment_form(forms.ModelForm):
    body = forms.CharField(max_length=500)


    class Meta:
        model = Comment
        fields = ('body',)
