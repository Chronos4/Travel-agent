from .models import UserProfile
from django import forms
from images.models import Image


class ProfileForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), label="About me")
    hobbies = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    places_been = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}), label="Places you haved been")
    places_to = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}), label="Places you are interested in ")

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user', 'active')


class PhotoUploadForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image']
