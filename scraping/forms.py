from .models import City, Language
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()

class FindForm(forms.Form):
	city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='slug', 
		required=False, widget=forms.Select(attrs={'class': 'form-control'}))
	language = forms.ModelChoiceField(queryset=Language.objects.all(), to_field_name='slug',
		required=False, widget=forms.Select(attrs={'class': 'form-control'}))


class UserLoginForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))




class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
      model = User
      fields = ['username', 'email', 'first_name']