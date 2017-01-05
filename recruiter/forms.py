from django import forms
from decimal import Decimal
from django.core.validators import EmailValidator,MinValueValidator
# from django.forms.Widget import attrs

class SearchApplicantForm(forms.Form):
	candidate_name = forms.CharField(
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Bruce Wayne'}),
		label="Condidate Name",
		required=False)

	email = forms.EmailField(
		widget=forms.EmailInput(attrs={
			'class':'form-control',
			'placeholder':'batty@wayne.com'}),
		label="Email",
		required=False,
		validators=[EmailValidator()])

	work_exp = forms.DecimalField(
		widget=forms.NumberInput(
			attrs={'class':'form-control has-popover',
			'placeholder':'2.5',
			'step':'0.50',
			'data-content':'Shows result having work experience <= provided range',
			'data-placement':'right',
			'data-container':'body',
			'data-toggle':'popover',}),
		label="Work Experience",
		required=False,
		validators=[MinValueValidator(Decimal(0.00))])

	current_loc = forms.CharField(
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Central City'}),
		label="Current Location",
		required=False)

	preffered_loc = forms.CharField(
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Gotham',}),
		label="Preferred Location",
		required=False)

	ctc = forms.DecimalField(
		widget=forms.NumberInput(attrs={
			'class':'form-control has-popover',
			'placeholder':'6.5',
			'step':'0.25',
			'data-content':'Shows result having CTC <= provided range',
			'data-placement':'right',
			'data-container':'body',
			'data-toggle':'popover'}),
		label="CTC",
		required=False,
		validators=[MinValueValidator(Decimal(0.00))])

	skills = forms.CharField(
		widget=forms.TextInput(attrs={
			'class':'form-control has-popover',
			'data-content':'skills can be comma seperated values',
			'data-placement':'right',
			'data-container':'body',
			'data-toggle':'popover',
			'placeholder':'html,css,django',}),
		label='Skills',
		required=False)

	ug_course = forms.CharField(
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'B.Tech'}),
		label="UG Course",
		required=False)

	ug_tire1 = forms.ChoiceField(
		widget=forms.Select(),
		choices=[(-1,None),(1,"Yes"),(2,"No")])

	pg_course = forms.CharField(
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'M.Tech'}),
		label="PG Course",required=False)

	pg_tire1 = forms.ChoiceField(
		widget=forms.Select(),
		choices=[(-1,None),(1,"Yes"),(2,"No")])