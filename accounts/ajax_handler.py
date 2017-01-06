from django.contrib.auth.models import User
from django.http import JsonResponse

def validate_username(request):
	username = request.GET.get('username',None)
	present = True
	try:
		user = User.objects.get(username__iexact=username)
	except User.DoesNotExist:
		present = False

	data = {
		'is_taken':present
	}

	if data['is_taken']:
		data['error_message']='Username already exist!'
	return  JsonResponse(data)

def validate_email(request):
	email = request.GET.get('email',None)
	present = True
	try:
		user = User.objects.get(email__iexact=email)
	except User.DoesNotExist:
		present = False
	data = {
		'email_exist':present
	}
	if data['email_exist']:
		data['error_message']='Email already registered!'
	return  JsonResponse(data)