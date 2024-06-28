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
def privacy(request):
	return render(request, 'renew/privacy.html', context)

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
	cases = Case.objects.filter(category_id=1)
	print(cases)

	if request.method == 'POST':
		callme_form = CallMeForm(request.POST)
		if callme_form.is_valid():
			callme = callme_form.save()
			send_email_task.delay(callme.first_name)
	else:
		callme_form = CallMeForm()

	context = {
		'callme_form': callme_form,
		'cases' : cases,
	}
	return render(request, 'renew/improvement.html', context)


def projection(request):
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
	return render(request, 'renew/projection.html', context)


def screening(request):
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
	return render(request, 'renew/screening.html', context)



def the_case(request, category=None, id=None):		
	if id:
		the_case = get_object_or_404(Case, id=id)
		similar_cases = Case.objects.filter(category=the_case.category)


	if request.method == 'POST':
		callme_form = CallMeForm(request.POST)
		if callme_form.is_valid():
			callme_form.save()
			send_email_task.delay(callme.first_name)
	else:
		callme_form = CallMeForm()

	context = {
		'the_case': the_case,
		'similar_cases': similar_cases,
		'callme_form': callme_form
	}
	return render(request, 'renew/the_case.html', context)



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