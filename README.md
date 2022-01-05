Here is a test REST API (backend app) which can be used to exchange information
with requests and responses between the server and the client in the appropriate form.

__________________________________________________________________________________________________________________________________

Here is the list of application's endpoints:

For drivers:
* GET /drivers/driver/                             - Display a list of drivers
* GET /drivers/driver/?created_at__gte=10-11-2021  - Display a list of drivers created after 10-11-2021
* GET /drivers/driver/?created_at__lte=16-11-2021  - Display a list of drivers created before 16-11-2021
* GET /drivers/driver/<driver_id>/                 - Receive information of a particular driver
* POST /drivers/driver/                            - Create a new driver
* DELETE /drivers/driver/<driver_id>/              - Delete information of a particular driver

For vehicles:
* GET /vehicles/vehicle/                          - Display a list of vehicles
* GET /vehicles/vehicle/?with_drivers=yes         - Display a list of vehicles with drivers
* GET /vehicles/vehicle/?with_drivers=no          - Display a list of vehicles without drivers
* GET /vehicles/vehicle/?with_driver/<vehicle_id>/ - Display if the driver is in the vehicle
* GET /vehicles/vehicle/<vehicle_id>              - Receive information about a specific vehicle
* POST /vehicles/vehicle/                         - Create a new one vehicle
* POST /vehicles/set_driver/<vehicle_id>/         - Put the driver in the car or get the driver out of the car
* DELETE /vehicles/vehicle/<vehicle_id>/          - Delete information about a specific vehicle

Note: "-" sign before the endpoint means that it isn't working yet

__________________________________________________________________________________________________________________________________

Admin profile:

Username: admin
Password: admin
E-mail: admin@example.com

