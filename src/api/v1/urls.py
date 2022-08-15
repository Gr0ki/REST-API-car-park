from django.urls import path, include

urlpatterns = [
    path("vehicles/", include("src.api.v1.vehicles.urls")),
    path("drivers/", include("src.api.v1.drivers.urls")),
]
