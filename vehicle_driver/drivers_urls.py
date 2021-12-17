from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^driver/$',                                  # GET, POST
            views.drivers_list,
            name='drivers-list'
            ),
    re_path(r'^driver/?created_at__gte=10-11-2021/$',      # GET
            views.drivers_list_after_date,
            name='drivers-list-after-date'
            ),
    re_path(r'^driver/?created_at__lte=16-11-2021/$',      # GET
            views.drivers_list_before_date,
            name='drivers-list-before-date'
            ),
    re_path(r'^driver/(?P<id>[0-9]+)/$',                    # GET, UPDATE (PATCH), DELETE
            views.driver_info,
            name='driver-info'
            ),
]
