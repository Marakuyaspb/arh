from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import CallMe, Case, Category


@admin.register(CallMe)
class CallMeAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'email','created']
	list_filter = ['created']