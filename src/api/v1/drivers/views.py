from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from ....vehicle_driver.serializers import DriverSerializer
from ....vehicle_driver.models import Driver


@api_view(["GET", "POST"])
def drivers_list(request):
    """
    Display a list of drivers or create a new one
    """
    if request.method == "GET":
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = DriverSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def drivers_list_after_date(request):
    """
    Display a list of drivers created after 10-11-2021
    """
    if request.method == "GET":
        try:
            driver = Driver.objects.filter(created_at__gte="2021-11-10")
            serializer = DriverSerializer(driver, many=True)
        except Driver.DoesNotExist:
            return JsonResponse({"status": 404}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
def drivers_list_before_date(request):
    """
    Display a list of drivers created before 16-11-2021
    """
    if request.method == "GET":
        try:
            driver = Driver.objects.filter(created_at__lte="2021-11-16")
            serializer = DriverSerializer(driver, many=True)
        except Driver.DoesNotExist:
            return JsonResponse({"status": 404}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["GET", "DELETE"])
def driver_info(request, driver_id):
    """
    Receive or delete information of a particular driver
    """
    try:
        driver = Driver.objects.get(id=driver_id)
    except Driver.DoesNotExist:
        return JsonResponse({"status": 404}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DriverSerializer(driver)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        driver.delete()
        serializer = DriverSerializer(driver)
        return JsonResponse(serializer.data, status=status.HTTP_204_NO_CONTENT)
