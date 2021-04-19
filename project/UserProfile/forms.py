from .models import UserProfile
from django import forms
from Authentication.models import CustomUser


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'image', 'bio']


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']