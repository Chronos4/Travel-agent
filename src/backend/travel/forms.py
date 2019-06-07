from django import forms
from .models import Destination_comment


class Comment_Form(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": 'form-control', 'rows': 3}), label="")

    class Meta:
        model = Destination_comment
        fields = ['content']
