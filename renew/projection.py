from django.shortcuts import render
import os
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template, render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


def index(request):
	return render(request, 'renew/index.html')

def improvement(request):
	return render(request, 'renew/improvement.html')

def projection(request):
	return render(request, 'renew/projection.html')
	
def screening(request):
	return render(request, 'renew/screening.html')