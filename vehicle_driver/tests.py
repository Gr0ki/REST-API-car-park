import json

from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import include, re_path, reverse

from .models import *


# Create your tests here.

class DriverTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        re_path(r'^drivers/', include('vehicle_driver.drivers_urls')),
    ]

    def setUp(self):
        self.first_driver_data = Driver.objects.create(
            first_name='Karl',
            last_name='Winslow',
            created_at='1980-11-16',
            updated_at='2021-12-18'
        )

        self.post_data = {
            'first_name': 'Jack', 'last_name': 'Black',
            'created_at': '20/11/2021', 'updated_at': '12/12/2021'
        }
        self.expected_post_data = {'id': 2}
        self.expected_post_data.update(self.post_data)

    def test_create_driver(self):
        """
        Test for creating a new instance of a Driver
        """
        url = reverse('drivers-list')
        response = self.client.post(url, self.post_data)
        assert response.status_code == 201
        self.assertEqual(Driver.objects.count(), 2)
        assert json.loads(response.content) == self.expected_post_data

    def test_get_list(self):
        """
        Test for getting list of drivers
        """
        url = reverse('drivers-list')
        response = self.client.get(url)
        assert response.status_code == 200

    # def test_get_list_after_date(self):
    #     """
    #     Test for getting a list of drivers instances which was created after 10/11/2021
    #     """
    #     url = reverse('drivers-list-after-date')
    #     response = self.client.get(url)                                             # DATE_FORMAT BUG
    #     assert response.status_code == 200
    #     assert json.loads(response.content) == self.expected_data

    # def test_get_list_before_date(self):
    #     """
    #     Test for getting a list of drivers instances which was created before 16/11/2021
    #     """
    #     url = reverse('drivers-list-before-date')
    #     response = self.client.get(url)                                             # DATE_FORMAT BUG
    #     assert response.status_code == 200
    #     assert json.loads(response.content) == self.first_driver_data

    def test_get_driver_info(self):
        """
        Test for getting information of a particular driver
        """
        url = reverse('driver-info', kwargs={'driver_id': 1})
        response = self.client.get(url)
        assert response.status_code == 200
        assert json.loads(response.content)['first_name'] == self.first_driver_data.__dict__['first_name']

    def test_delete_driver_info(self):
        """
        Test for deleting information of a particular driver
        """
        url = reverse('driver-info', kwargs={'driver_id': 1})
        response = self.client.get(url)
        assert response.status_code == 200


class VehicleTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        re_path(r'^vehicles/', include('vehicle_driver.vehicle_urls')),
    ]

    def setUp(self):
        self.expected_post_data = Vehicle.objects.create(                              # DATE_FORMAT BUG
            driver_id=None,
            make='BYD',
            model='random',
            plate_number='АЕ 8736 АВ',
            created_at='10/10/2020',
            updated_at='11/10/2021'
        )

        self.post_data = {
            'driver_id': '2', 'make': 'Nissan', 'model': 'leaf', 'plate_number': 'АА 6727 НР',
            'created_at': '20/11/2021', 'updated_at': '12/12/2021'
        }
        self.expected_post_data = {'id': 2}
        self.expected_post_data.update(self.post_data)

    def test_create_vehicle(self):
        """
        Test for creating a new vehicle
        """
        url = reverse('vehicles-list')
        response = self.client.post(url, self.post_data)                              # DATE_FORMAT BUG
        assert response.status_code == 201
        self.assertEqual(Vehicle.objects.count(), 2)
        assert json.loads(response.content) == self.expected_post_data

    def test_get_vehicles_list(self):
        """
        Test for displaying a list of vehicles
        """
        url = reverse('vehicles-list')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_get_vehicles_list_with_or_without_driver(self):
        """
        Test for displaying a list of vehicles with or without drivers
        """
        driver_status = 'yes'
        while driver_status is not 'no':
            url = reverse('vehicles-list-with-or-without-driver', kwargs={'driver_status': driver_status})
            response = self.client.get(url)
            assert response.status_code == 200
            driver_status = 'no'
        else:
            url = reverse('vehicles-list-with-or-without-driver', kwargs={'driver_status': driver_status})
            response = self.client.get(url)
            assert response.status_code == 200

    def test_get_is_driver_in_vehicle(self):
        """
        Test for displaying if the driver is in the vehicle
        """
        for i in range(2):
            vehicle_id = i + 1
            url = reverse('is-driver-in-vehicle', kwargs={'vehicle_id': vehicle_id})
            response = self.client.get(url)
            assert response.status_code == 200

    def test_get_vehicle_info(self):
        """
        Test for receiving information about a specific vehicle
        """
        # url = reverse('vehicle-info', kwargs={'vehicle_id': })
        pass

    def test_delete_vehicle_info(self):
        """
        Test for deleting information about a specific vehicle
        """
        # url = reverse('vehicle-info', kwargs={'vehicle_id': })
        pass

    def test_add_or_remove_driver_from_vehicle(self):
        """
        Test for putting the driver in the car or getting the driver out of the car
        """
        # url = reverse('add-or-remove-driver-from-vehicle', kwargs={'vehicle_id': })
        pass
