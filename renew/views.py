from django.shortcuts import render
import os
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template, render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from .models import CallMe, Case, Category
from .forms import CallMeForm


def error_404_view(request, exception):
	return render(request, '404.html', status=40)

def index(request):
	return render(request, 'renew/index.html')

def improvement(request):
	return render(request, 'renew/improvement.html')
def privacy(request):
	return render(request, 'renew/privacy.html')
def projection(request):
	return render(request, 'renew/projection.html')	
def screening(request):
	return render(request, 'renew/screening.html')


def case(request, product_slug=None):
	callme_form = CallMeForm()

	if product_slug:
		case = get_object_or_404(Case, id=id)
		similar_cases = Case.objects.filter(category=case.category)

		return render(request, 'renew/the_case.html', {
			'case': case,
			'similar_cases': similar_cases
			}
		)