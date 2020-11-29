from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.utils import timezone
import datetime

class RegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            '__all__'
        )

    def clean(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        password2 = self.cleaned_data["password2"]
        if password != password2:
            raise forms.ValidationError("Your passwords do not match. Please try again.")

        email_taken = User.objects.filter(email=email)

        if email_taken:
                raise forms.ValidationError({'email':["There is already an existing account with that email address."]})
                return self
        return self.cleaned_data