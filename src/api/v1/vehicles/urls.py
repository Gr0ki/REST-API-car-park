from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r"^vehicle/$", views.vehicles_list, name="vehicles-list"),  # GET, POST
    re_path(
        r"^vehicle/?with_drivers=(?P<driver_status>yes|no)/$",  # GET
        views.vehicles_list_with_or_without_driver,
        name="vehicles-list-with-or-without-driver",
    ),
    re_path(
        r"^vehicle/?with_driver/(?P<vehicle_id>[0-9]+)/$",  # GET
        views.is_driver_in_vehicle,
        name="is-driver-in-vehicle",
    ),
    re_path(
        r"^vehicle/(?P<vehicle_id>[0-9]+)/$",  # GET, DELETE
        views.vehicle_info,
        name="vehicle-info",
    ),
    re_path(
        r"^set_driver/(?P<vehicle_id>[0-9]+)/$",  # POST
        views.add_or_remove_driver_from_vehicle,
        name="add-or-remove-driver-from-vehicle",
    ),
]
