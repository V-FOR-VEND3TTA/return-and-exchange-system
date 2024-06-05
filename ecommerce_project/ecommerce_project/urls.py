from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, 'returns_exchanges/404.html', status=404)

handler404 = custom_404

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('my_admin/', admin.site.urls),
    path('', include('returns_exchanges.urls')),
]
