from django.db import models
from decimal import Decimal
from django.core.validators import RegexValidator,MinValueValidator
from django.contrib.auth.models import AbstractBaseUser

class Applicant(models.Model):
	resume = models.CharField(max_length=3)
	candidate_name = models.CharField(max_length=50)
	mobile_regex = RegexValidator(
		regex=r'^\+?\d{8,15}$',
		message='Invalid mobile number')
	mobile_number = models.CharField(
		max_length=15,validators=[mobile_regex],
		blank=True)
	email = models.EmailField(unique=True)
	work_exp = models.DecimalField(
		max_digits=5,decimal_places=2,
		default=Decimal(0.00),
		validators=[MinValueValidator(Decimal('0.00'))])
	analytics_exp = models.DecimalField(
		max_digits=5,decimal_places=2,
		default=Decimal(0.00))
	current_loc = models.CharField(max_length=100)
	corrected_city = models.CharField(max_length=50)
	nearest_city = models.CharField(max_length=50)
	preffered_loc = models.CharField(max_length=100)
	ctc = models.DecimalField(
		max_digits=10,decimal_places=2,
		default=Decimal(0.00),
		validators=[MinValueValidator(Decimal('0.00'))],
		null=True,
		blank=True,)
	current_employer = models.CharField(
		max_length=50,
		blank=True)
	current_designation = models.CharField(
		max_length=50,
		blank=True)
	skills = models.CharField(
		max_length=200,
		blank=True)
	ug_course = models.CharField(
		max_length=30,)
	ug_institute_name = models.CharField(
		max_length=50,)
	ug_passing_year = models.PositiveSmallIntegerField(null=True,blank=True)
	ug_tire1 = models.CharField(
		max_length=3,
		default='No',)
	pg_course = models.CharField(
		max_length=30,
		blank=True)
	current_pg_course = models.CharField(
		max_length=30,
		blank=True)
	pg_institute_name = models.CharField(
		max_length=50,
		blank=True)
	pg_tire1 = models.CharField(
		max_length=3,
		default='No',
		blank=True)
	pg_passing_year = models.PositiveSmallIntegerField(null=True,blank=True)
	post_pg_course = models.CharField(
		max_length=30,
		blank=True)
	current_post_pg_course = models.CharField(
		max_length=30,
		blank=True)

	def __str__(self):
		return self.candidate_name