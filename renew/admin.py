from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import CallMe, Case, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id_cat', 'category']
	list_filter = ['category']


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
	list_display = ['id', 'category', 'name', 'square', 'year']
	list_filter = ['name']


@admin.register(CallMe)
class CallMeAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'email','created']
	list_filter = ['created']