from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

class RegistrationForm(forms.ModelForm):
	"""
		User Registration form
	"""
	username = forms.CharField(
		widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'User Name',}),
		required=True,)

	email = forms.EmailField(
		widget=forms.EmailInput(attrs={
			'class':'form-control',
			'placeholder':'E-mail'}),
		required=True,
		validators=[EmailValidator()])

	password1 = forms.CharField(
		widget=forms.PasswordInput(),
		label="Password")

	password2 = forms.CharField(
		widget=forms.PasswordInput(),
		label="Confirm Password")

	class Meta:
		model = User
		fields = ['username','email','password1','password2']

	def clean(self):
		"""
		Verifies that the values entered into the password fields match
		"""
		cleaned_data = super(RegistrationForm, self).clean()
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
			return self.cleaned_data

	def clean_username(self):
		"""
		Verifies that the username entered is unique and not already exist
		"""
		try:
			user = User.objects.get(username__iexact=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
			raise forms.ValidationError(_("The username already exists. Please try another one."))

	def clean_email(self):
		"""
		Verifies that the email entered is unique and not already exist
		"""
		try:
			user = User.objects.get(email__iexact=self.cleaned_data['email'])
		except User.DoesNotExist:
			return self.cleaned_data['email']
			raise forms.ValidationError(_("The email already exists. Please try another one."))

class LoginForm(forms.Form):
	"""
		User Login Form
	"""
	email = forms.EmailField(
		widget=forms.EmailInput(attrs={
			'class':'form-control',
			'placeholder':'E-mail'}),
		required=True,
		validators=[EmailValidator()])

	password = forms.CharField(
		widget=forms.PasswordInput(),
		label="Password")