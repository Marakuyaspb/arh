from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'renew'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('improvement/', views.improvement, name = 'improvement'),
    path('all_news/', views.all_news, name = 'all_news'),
    path('privacy/', views.privacy, name = 'privacy'),
    path('projection/', views.projection, name = 'projection'),
    path('screening/', views.screening, name = 'screening'),
    path('<slug:category>/<int:id>/', views.the_case, name='case'),
    path('<category>/<int:id>/', views.the_case, name='the_case'),
]