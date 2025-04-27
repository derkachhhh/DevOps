from django.contrib import admin
from django.urls import path, include
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from django.http import HttpResponse

def metrics_view(request):
    metrics_page = generate_latest()
    return HttpResponse(metrics_page, content_type=CONTENT_TYPE_LATEST)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newss.urls')),
    path('metrics', metrics_view),  # ➔ тепер правильно
]

