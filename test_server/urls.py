from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^drivers/', include('vehicle_driver.drivers_urls')),
    re_path(r'^vehicles/', include('vehicle_driver.vehicle_urls')),
]
