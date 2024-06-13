import os
from .models import CallMe, Case, Category
from .forms import CallMeForm
from .tasks import send_email_task

from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.template.loader import get_template, render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

import weasyprint
from weasyprint import HTML
import logging
from django.core.mail import send_mail, send_mass_mail



def error_404_view(request, exception):
	return render(request, 'renew/404.html', status=404)

def index(request):
	if request.method == 'POST':
		callme_form = CallMeForm(request.POST)
		if callme_form.is_valid():
			callme = callme_form.save()
			send_email_task.delay(callme.first_name)
	else:
		callme_form = CallMeForm()

	context = {
		'callme_form': callme_form
	}

	return render(request, 'renew/index.html', context)


def improvement(request):
	return render(request, 'renew/improvement.html')
def privacy(request):
	return render(request, 'renew/privacy.html')
def projection(request):
	return render(request, 'renew/projection.html')	
def screening(request):
	return render(request, 'renew/screening.html')


def case(request, product_slug=None):
	if request.method == 'POST':
		callme_form = CallMeForm(request.POST)
		if callme_form.is_valid():
			callme_form.save()
			send_email_task.delay(callme.first_name)
	else:
		callme_form = CallMeForm()

	context = {
		'callme_form': callme_form
	}



	if id:
		case = get_object_or_404(Case, id=id)
		similar_cases = Case.objects.filter(category=case.category)

		return render(request, 'renew/the_case.html', {
			'case': case,
			'similar_cases': similar_cases,
			'callme_form': callme_form
			}
		)



# MAIL
logging.basicConfig(filename='mail_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')



def new_callme(request):
	if request.method == 'POST':
		callme_form = CallMeForm(request.POST)
		if callme_form.is_valid():
			callme_form.save()
			send_email_task.delay(callme.first_name)
	else:
		callme_form = CallMeForm()

	context = {
		'callme_form': callme_form
	}
