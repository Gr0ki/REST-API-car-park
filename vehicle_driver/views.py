from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import DriverSerializer, VehicleSerializer
from .models import Driver, Vehicle


@api_view(['GET', 'POST'])
def driver_list(request):
    if request.method == 'GET':
        # вивід списку водіїв
        pass
    elif request.method == 'POST':
        # створення нового водія
        pass


@api_view(['GET'])
def drivers_list_after_date(request):
    if request.method == 'GET':
        # вивід списку водіїв, які створені після 10-11-2021
        pass


@api_view(['GET'])
def drivers_list_before_date(request):
    if request.method == 'GET':
        # вивід списку водіїв, котрі створені до 16-11-2021
        pass


# 'PATCH'?
@api_view(['GET', '', 'DELETE'])
def driver_info(request, id):
    if request.method == 'GET':
        # отримання інформації по певному водію
        pass
    elif request.method == '':
        # редагування водія
        pass
    elif request.method == 'DELETE':
        # видалення водія
        pass


@api_view(['GET', 'POST'])
def vehicle_list(request):
    if request.method == 'GET':
        # вивід списку машин
        pass
    elif request.method == 'POST':
        # створення нової машини
        pass


@api_view(['GET'])
def vehicle_list_with_or_without_driver(request, status):
    if request.method == 'GET':
        # вивід списку машин з водіями чи без водіїв
        pass


# 'PATCH'?
@api_view(['GET', '', 'DELETE'])
def vehicle_info(request, vehicle_id):
    if request.method == 'GET':
        # отримання інформації по певній машині
        pass
    elif request.method == '':
        # редагування машини
        pass
    elif request.method == 'DELETE':
        # видалення машини
        pass


@api_view(['POST'])
def add_or_remove_driver_from_vehicle(request, vehicle_id):
    if request.method == 'POST':
        # садимо водія в машину / висаджуєм водія з машини
        pass
