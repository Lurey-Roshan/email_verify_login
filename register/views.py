from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from register.forms import SignupForm ,LoginForm
from django.contrib.auth import authenticate, login, logout
from verify_email.email_handler import send_verification_email
# Create your views here.
def home(request):
	return render(request,'home.html')


def login(request):
	form=LoginForm()
	if request.method=="POST":
		form=LoginForm(request.POST)
		username=form.get('username')
		password=form.get('password')
	context={
		'form':form
	}

	return render(request, 'login.html', context)
def signup(request):
	form=SignupForm()
	if request.method=="POST":
		form=SignupForm(request.POST)
		if form.is_valid():
			inactive_user = send_verification_email(request, form)

			form.save()
			messages.success(request,"Your account has been Created, Please validate your email")
			return redirect('login')
		else:
			messages.error(request, "Please Provide valid data")
			form=SignupForm()
	context={
		'form':form,
		'messages':messages
	}
	return render(request,'signup.html', context)


def log_in(request):
	form=LoginForm()
	if request.method=="POST":
		form=LoginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			if username.is_email():
				user=authenticate(request,username=username, password=password)
				if user is  not None:
					login(request, user)
			else:
				user=authenticate(request,username=username, password=password)
				if user is  not None:
					login(request, user)
		else:
			return HttpResponse(request,"Please Provide Correct Username and password")
	context={
		'form':form
	}
	return render(request,'login.html', context)


def log_out(request):
	user=request.user
	logout(request, user)
	messages.success(request, 'successfully Logged out')
	return redirect('home')