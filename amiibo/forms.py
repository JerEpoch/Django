from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Amiibo
from django.forms import ModelForm, TextInput

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class AmiiboForm(ModelForm):

    class Meta:
        model = Amiibo
        fields = ('name','series','price')

    price=forms.CharField(label='Price', widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'test'}
    ))
