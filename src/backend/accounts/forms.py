import datetime
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
User = get_user_model()

choices_gender = (
    ('male', 'Male'),
    ('female', 'Female')
)


class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': '**********', 'id': 'register-staff'}))
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder': '**********', 'id': 'register-staff'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'age', 'gender')

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your Email', 'id': 'register-staff'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your First Name', 'id': 'register-staff'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your Last Name', 'id': 'register-staff'}),
            'age': forms.TextInput(attrs={'id': 'register-staff'}),
            'gender': forms.Select(attrs={'id': 'register-gender'})
        }

    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('__all__')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdminCreateForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'age', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
