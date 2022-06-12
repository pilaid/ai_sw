from django.contrib import admin
from django.urls import path
from landing.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)