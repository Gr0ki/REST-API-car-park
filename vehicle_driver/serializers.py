from rest_framework import serializers
from vehicle_driver.models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = (
                  'id',
                  'first_name',
                  'last_name',
                  'created_at',
                  'updated_at',
                  )


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = (
                  'id',
                  'driver_id',
                  'make',
                  'model',
                  'plate_number',
                  'created_at',
                  'updated_at'
                  )
