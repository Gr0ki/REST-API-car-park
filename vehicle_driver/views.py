from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import DriverSerializer, VehicleSerializer
from .models import Driver, Vehicle


@api_view(['GET', 'POST'])
def driver_list(request):
    """
    Display a list of drivers or create a new one
    """
    if request.method == 'GET':
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DriverSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def drivers_list_after_date(request):
    """
    Display a list of drivers created after 10-11-2021
    """
    if request.method == 'GET':
        try:
            driver = Driver.objects.filter(created_at__gte='2021-11-10')
            serializer = DriverSerializer(driver, many=True)
        except Driver.DoesNotExist:
            return HttpResponse(status=404)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def drivers_list_before_date(request):
    """
    Display a list of drivers created before 16-11-2021
    """
    if request.method == 'GET':
        try:
            driver = Driver.objects.filter(created_at__lte='2021-11-16')
            serializer = DriverSerializer(driver, many=True)
        except Driver.DoesNotExist:
            return HttpResponse(status=404)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


# 'PATCH'?
@api_view(['GET', 'UPDATE', 'DELETE'])
def driver_info(request, id):
    """
    Receive, edit, or delete information of a particular driver
    """
    try:
        driver = Driver.objects.get(id=id)
    except Driver.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DriverSerializer(driver)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    #elif request.method == 'PATCH':
        #data = JSONParser().parse(request)
        #serializer = DriverSerializer(driver, data=data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return JsonResponse(serializer.data)
        #return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        driver.delete()
        serializer = DriverSerializer(driver)
        return JsonResponse(serializer.data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def vehicle_list(request):
    """
    Display a list of vehicles or create a new one
    """
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def vehicle_list_with_or_without_driver(request, driver_status):
    """
    Display a list of vehicles with or without drivers
    """
    if request.method == 'GET' and driver_status == 'yes':
        try:
            vehicles = Vehicle.objects.filter(driver_id__isnull=True)
            serializer = VehicleSerializer(vehicles, many=True)
        except Vehicle.DoesNotExist:
            return HttpResponse(status=404)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'GET' and driver_status == 'no':
        try:
            vehicles = Vehicle.objects.filter(driver_id__isnull=False)
            serializer = VehicleSerializer(vehicles, many=True)
        except Vehicle.DoesNotExist:
            return HttpResponse(status=404)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


# 'PATCH'?
@api_view(['GET', 'UPDATE', 'DELETE'])
def vehicle_info(request, vehicle_id):
    """
    Receive, edit, or delete information about a specific vehicle
    """
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
        serializer = VehicleSerializer(vehicle)
    except Vehicle.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    # elif request.method == 'PATCH':
    # data = JSONParser().parse(request)
    # serializer = VehicleSerializer(vehicle, data=data)
    # if serializer.is_valid():
    #    serializer.save()
    #    return JsonResponse(serializer.data)
    # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vehicle.delete()
        return JsonResponse(serializer.data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_or_remove_driver_from_vehicle(request, vehicle_id):
    """
    Put the driver in the car or get the driver out of the car
    """
    #Need to take only one field for update

    #if request.method == 'POST':
    #    serializer = VehicleSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    #    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


