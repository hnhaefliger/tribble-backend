from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def empty(request):
    return HttpResponse('wakemydyno', content_type="text/plain")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/session/', include('browser_sessions.urls')),
]
