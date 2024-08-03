from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'address']
