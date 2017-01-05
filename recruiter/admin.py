from django.contrib import admin
from .models import Applicant

class ApplicantAdmin(admin.ModelAdmin):
	list_display = ('candidate_name','email','mobile_number','work_exp','current_loc','skills')
	search_fields = ('candidate_name', 'skills','work_exp')
	list_filter = ('work_exp',)
	ordering = ('candidate_name',)

admin.site.register(Applicant,ApplicantAdmin)