from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

from renew import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('renew.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)