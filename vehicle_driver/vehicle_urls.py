from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^vehicle/$', views.vehicle_list),                        # GET, POST
    re_path(r'^with_drivers=(?P<driver_status>yes|no)/$',
            views.vehicle_list_with_or_without_driver),                # GET
    re_path(r'^vehicle/(?P<vehicle_id>[0-9]+)/$',
            views.vehicle_info),                                       # GET, UPDATE (PATCH), DELETE
    re_path(r'^set_driver/(?P<vehicle_id>[0-9]+)/$',
            views.add_or_remove_driver_from_vehicle),                  # POST
]
