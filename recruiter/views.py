from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SearchApplicantForm
from .models import Applicant
import csv

BOOL_VALUES={'1':'Yes','2':'No'}

class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        return value

@login_required
def create_csv_stream(request):
	"""A view that streams a large CSV file."""
	# Generate a sequence of rows. The range is based on the maximum number of
	# rows that can be handled by a single sheet in most spreadsheet
	# applications.    
	form = SearchApplicantForm(request.POST)
	results,headers = _search(request,form,request.session['filter_request'])
	results=[obj for obj in results]
	results.insert(0,headers)
	pseudo_buffer = Echo()
	writer = csv.writer(pseudo_buffer)
	response = StreamingHttpResponse((writer.writerow(row) for row in results),content_type="text/csv")
	response['Content-Disposition'] = 'attachment; filename="applicant_record.csv"'
	return response

def _perform_search(field_values):
	"""
	private function of search to search db 
	arguments : field_value
	field_value is a list of filed value  
	"""
	filter_list={}
	for(key,value) in field_values.items():
		if(value != '' and value != None and value != '-1' and key!='csrfmiddlewaretoken'):
			if(value in BOOL_VALUES):
				filter_list[key]=BOOL_VALUES[value]
			else:
				if key == 'search':
					key = key + '__in'
					value = [x.strip(' ') for x in value.split(',')]
				if key=='candidate_name' or key == 'current_loc' or key == 'preffered_loc' or key == 'skills' :
					key = key + '__icontains'
				if key=='ctc' or key=='work_exp':
					key = key + '__lte'
				filter_list[key]=value
	results = Applicant.objects.filter(**filter_list).values_list()
	return results

def _search(request,form,fields=None):
	"""
	Private helper function of search method
	argument : form,fields
	form : it's a instance SearchApplicantForm
	fields : let search database by provided dictionary of filter fields
	TODO : performance update (skills field)
	"""
	# attributes = [field.name for field in Applicant._meta.get_fields()]
	attributes = ['Resume','Candidate Name','Mobile','Email','Work Exp.','Analytic Exp.','Current Location','Corrected City','Nearest City',
	'Preferred City','CTC','Current Employer','Current Designation','Skills','UG Course','UG Institute','UG Passing Yr.','UG Tire1',
	'PG Course','Current PG Course','PG Institute','PG Tire1','PG Passing Yr.','Post PG Course','Current Post PG Course']
	results = None
	if fields == None:
		if form.is_valid():
			cd = form.cleaned_data
			
			#filter_request keep the (key,value) pair used to filter database upon last request
			request.session['filter_request'] = request.POST

			results = _perform_search(cd)
	else:
		results = _perform_search(fields)

	return results,attributes

def search(request):
	"""
	Search the database
	"""
	if request.method == 'POST':
		form = SearchApplicantForm(request.POST)
		results,attributes = _search(request,form)
		if(results != None and attributes != None):
			return render(request,'search_form.html',{'form':form,'results':results,'attributes':attributes,'submitted':True,'request':request})
		else:
			return render(request,'search_form.html',{'form':form,'request':request})
	else:
		form = SearchApplicantForm()
		return render(request,'search_form.html',{'form':form,'request':request})