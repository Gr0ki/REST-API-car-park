from django.db import models
from django.core.exceptions import ValidationError
from re import fullmatch

# Create your models here.


class Driver(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"


def validate_plate_number(value):
    if fullmatch('(([А-ЯҐЄІЇ]{2})|([А-Я]{2})|([A-Z]{2}))[ ][0-9]{4}[ ](([А-ЯҐЄІЇ]{2})|([А-Я]{2}))', value) is not None:
        return value
    else:
        raise ValidationError(
            'Inappropriate format. Try to use Ukrainian letters, example: "AA 1234 OO".'
            )


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    make = models.CharField(max_length=254)
    model = models.CharField(max_length=254)
    plate_number = models.CharField(
                                    max_length=10,
                                    validators=[validate_plate_number])
    created_at = models.DateField()
    updated_at = models.DateField()

    def is_driver_without_vehicle(self):
        if self.driver_id is None:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.id}: {self.make} {self.model} - {self.plate_number}"
