from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignupForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username', 'email', 'first_name','last_name','password1','password2']
		widgets={
			'username':forms.TextInput(),
			'email':forms.EmailInput(),
			'first_name':forms.TextInput(),
			'last_name':forms.TextInput(),
			'password1':forms.PasswordInput(),
			'password2':forms.PasswordInput()
		}

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100)
	password=forms.CharField(label='Password')