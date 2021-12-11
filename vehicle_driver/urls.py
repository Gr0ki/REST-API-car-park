from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^/drivers/driver/$', views.driver_list),                 # GET, POST
    re_path(r'^/drivers/driver/?created_at__gte=10-11-2021$',
            views.drivers_list_after_date),                            # GET
    re_path(r'^/drivers/driver/?created_at__lte=16-11-2021$',
            views.drivers_list_before_date),                           # GET
    re_path(r'^/drivers/driver/(?P<id>[0-9]+)/$', views.driver_info),  # GET, UPDATE (PATCH), DELETE

    re_path(r'^/vehicles/vehicle/$', views.vehicle_list),              # GET, POST
    re_path(r'^/vehicles/vehicle/?with_drivers=(?P<status>yes|no)$',
            views.vehicle_list_with_or_without_driver),                # GET
    re_path(r'^/vehicles/vehicle/(?P<vehicle_id>[0-9]+)/$',
            views.vehicle_info),                                       # GET, UPDATE (PATCH), DELETE
    re_path(r'^/vehicles/set_driver/(?P<vehicle_id>[0-9]+)/$',
            views.add_or_remove_driver_from_vehicle),                  # POST
]
