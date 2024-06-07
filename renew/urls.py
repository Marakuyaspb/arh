from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from renew import views

app_name = 'renew'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('improvement/', views.improvement, name = 'improvement'),
    path('projection/', views.projection, name = 'projection'),
    path('screening/', views.screening, name = 'screening')
]