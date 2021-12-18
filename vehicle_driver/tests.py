import json

from django.core import serializers
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import include, re_path, reverse

from .models import *


# Create your tests here.
from .serializers import DriverSerializer


class DriverTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        re_path(r'^drivers/', include('vehicle_driver.drivers_urls')),
    ]

    def setUp(self):                                                      # Random order?
        self.post_data = {
            'first_name': 'Jack', 'last_name': 'Black',
            'created_at': '20/11/2021', 'updated_at': '12/12/2021'
        }
        self.expected_data = {'id': 1}
        self.expected_data.update(self.post_data)

    def test_create(self):
        """
        Test of creating a new instance of a Driver
        """
        url = reverse('drivers-list')
        response = self.client.post(url, self.post_data)
        assert response.status_code == 201
        self.assertEqual(Driver.objects.count(), 1)
        assert json.loads(response.content) == self.expected_data

    def test_get_list(self):
        """
        Test of getting list of drivers
        """
        url = reverse('drivers-list')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_get_list_after_date(self):
        """
        Test of getting a list of drivers instances which was created after 10/11/2021
        """
        url = reverse('drivers-list-after-date')
        response = self.client.get(url)                                             # DATE_FORMAT BUG
        assert response.status_code == 200
        assert json.loads(response.content) == self.expected_data

    def test_get_list_before_date(self):
        """
        Test of getting a list of drivers instances which was created before 16/11/2021
        """
        url = reverse('drivers-list-before-date')
        query = Driver.objects.create(
            first_name='Karl',
            last_name='Winslow',
            created_at='1980-11-16',
            updated_at='2021-12-18'
        )
        serializer = DriverSerializer(query)
        self.expected_data = serializers.deserialize("json", serializer)
        response = self.client.get(url)                                             # DATE_FORMAT BUG
        assert response.status_code == 200
        assert json.loads(response.content) == self.expected_data

    def test_get_driver_info(self):
        """
        Test of getting information of a particular driver
        """
        url = reverse('driver-info', kwargs={'driver_id': 1})
        response = self.client.get(url)
        print(response.status_code)
        assert response.status_code == 200                                  # ERROR: response.status_code = 404
        self.setUp()
        assert json.loads(response.content) == self.expected_data
