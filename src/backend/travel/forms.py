from django import forms
from .models import Destination_comment, Adventure, countries


class Comment_Form(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": 'form-control', 'rows': 3}), label="")

    class Meta:
        model = Destination_comment
        fields = ['content']


class Create_form(forms.ModelForm):
    country = forms.CharField(
        label="Country", widget=forms.Select(choices=countries, attrs={"id": "country-field"}))

    town = forms.CharField(label="Town:", widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "town-field"
    }))
    commentaries = forms.CharField(label="Commentaries:", widget=forms.Textarea(attrs={
        "class": "form-control",
        'id': "commentaries-field",
        'rows': 2,
    }))

    class Meta:
        model = Adventure
        fields = ['country', 'image',
                  'town', 'commentaries', 'start', 'end']
