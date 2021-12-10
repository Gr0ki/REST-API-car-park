from django.db import models
from django.core.exceptions import ValidationError
from re import fullmatch

# Create your models here.


class Driver(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateField()
    updated_at = models.DateField()


def validate_plate_number(value):
    if fullmatch('[А-ЯҐЄІЇ]{2}[ ][0-9]{4}[ ][А-ЯҐЄІЇ]{2}', value) is not None:
        return value
    else:
        raise ValidationError('Inappropriate format. Example: "AA 1234 OO"')


class Vehicle(models.Model):
    # id = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plate_number = models.CharField(
                        max_length=10,
                        validators=[validate_plate_number]
                        )
    created_at = models.DateField()
    updated_at = models.DateField()
