from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(label="", max_length="30",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password1 = forms.CharField(label="", max_length="30",
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="", max_length="30",
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class SignInForm(AuthenticationForm):
    username = forms.CharField(label="", max_length="30",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(label="", max_length="30",
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ("username", 'password')
