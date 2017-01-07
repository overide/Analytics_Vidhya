from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import check_password

@csrf_protect
def register(request):
	"""
	Procedure to register user
	"""
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid() and form.clean_username() and form.clean_email():
			user = User.objects.create_user(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
				email = form.cleaned_data['email'])
			request.session['is_logged'] = True
			request.session['u_name'] = form.cleaned_data['username'].upper()

			#filter_request keep the (key,value) pair used to filter database upon last request
			request.session['filter_request'] = request.POST 		

			return HttpResponseRedirect('/recruiter/search/')
		else:
			return render(request,'index.html')
	else:
		return render(request,'index.html')

def custom_authenticate(email,pswrd):
	"""
		Custom authentication method which take email and password to authenticate user
		rather than Django's default authentication based on username,password 
	"""
	user = User.objects.filter(email__iexact = email)
	if user:
		if check_password(pswrd,user[0].password):
			u_name = user[0].username
			user = authenticate(username=u_name,password=pswrd)
			return user
	return None

def login_view(request):
	"""
	Authenticate user upon email and password provided
	"""
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = custom_authenticate(email,password)
			if user is not None:
				if user.is_active:
					login(request,user)
					request.session['is_logged'] = True
					request.session['u_name'] = user.username.upper()
					request.session['filter_request'] = None
					return HttpResponseRedirect('/recruiter/search/')
				else:
					errors=["This account is disabled!",]
					return render(request,'error_page.html',{'errors':errors,})
			else:
				errors = ["Invalid username or password!",]
				return render(request,'index.html',{'errors':errors,})
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def logout_view(request):
	"""
	Logging out logged in user
	"""
	logout(request)
	return HttpResponseRedirect('/') #back to homepage