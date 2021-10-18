from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', )


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']