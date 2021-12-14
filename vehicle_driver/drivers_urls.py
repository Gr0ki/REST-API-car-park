from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^driver/$', views.driver_list),                          # GET, POST
    re_path(r'^driver/?created_at__gte=10-11-2021/$',
            views.drivers_list_after_date),                            # GET
    re_path(r'^driver/?created_at__lte=16-11-2021/$',
            views.drivers_list_before_date),                           # GET
    re_path(r'^driver/(?P<id>[0-9]+)/$', views.driver_info),           # GET, UPDATE (PATCH), DELETE
]
