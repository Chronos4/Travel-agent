from django import forms
from .models import Destination_comment, Adventure


class Comment_Form(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": 'form-control', 'rows': 3}), label="")

    class Meta:
        model = Destination_comment
        fields = ['content']


class Create_form(forms.ModelForm):
    town = forms.CharField(label="Town:", widget=forms.TextInput(attrs={
        "class": "form-control",
        "cols": 1
    }))
    commentaries = forms.CharField(label="Commentaries:", widget=forms.Textarea(attrs={
        "class": "form-control",
        'rows': 3
    }))

    class Meta:
        model = Adventure
        fields = ['country', 'image',
                  'town', 'commentaries', 'start', 'end']
