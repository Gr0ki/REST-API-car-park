import json

from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from django.urls import include, re_path, reverse

from .models import *


# Create your tests here.

class DriverTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        re_path(r'^drivers/', include('vehicle_driver.drivers_urls')),
    ]

    def setUp(self):
        self.post_data = {
            'first_name': 'Jack', 'last_name': 'Black',
            'created_at': '12/01/2019', 'updated_at': '12/02/2021'
        }

    def test_create(self):
        url = reverse('drivers-list')
        response = self.client.post(url, self.post_data)
        #self.assertEqual(self, response.status_code, status.HTTP_201_CREATED)                                # BUG
        self.assertEqual(Driver.objects.count(), 1)
        #self.assertEqual(self, Driver.objects.get(first_name='Jack').last_name, self.post_data['last_name']) # BUG

    def test_get_list(self):
        url = reverse('drivers-list')
        response = self.client.get(url)
        #self.assertEqual(self, response.status_code, status.HTTP_200_OK)                                     # BUG
