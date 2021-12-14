Here is a test REST API (backend app) which can be used to exchange information
with requests and responses between the server and the client in the appropriate form.

_____________________________________________________________________________________________________________

Here is the list of application's endpoints:

For drivers:
* GET /drivers/driver/                             - Display a list of drivers
* GET /drivers/driver/?created_at__gte=10-11-2021  - Display a list of drivers created after 10-11-2021
* GET /drivers/driver/?created_at__lte=16-11-2021  - Display a list of drivers created before 16-11-2021
* GET /drivers/driver/<driver_id>/                 - Receive information of a particular driver
* POST /drivers/driver/                            - Create a new driver
- UPDATE /drivers/driver/<driver_id>/              - Edit information of a particular driver
* DELETE /drivers/driver/<driver_id>/              - Delete information of a particular driver

For vehicles:
* GET /vehicles/vehicle/                          - Display a list of vehicles
* GET /vehicles/vehicle/?with_drivers=yes         - Display a list of vehicles with drivers
* GET /vehicles/vehicle/?with_drivers=no          - Display a list of vehicles without drivers
* GET /vehicles/vehicle/<vehicle_id>              - Receive information about a specific vehicle
* POST /vehicles/vehicle/                         - Create a new one vehicle
- UPDATE /vehicles/vehicle/<vehicle_id>/          - Edit information about a specific vehicle
- POST /vehicles/set_driver/<vehicle_id>/         - Put the driver in the car or get the driver out of the car
* DELETE /vehicles/vehicle/<vehicle_id>/          - Delete information about a specific vehicle

Note: "-" sign before the endpoint means that it isn't working yet

_____________________________________________________________________________________________________________

The main settings of a project is in test_server folder while all functionality of an app
is in vehicle_driver folder.

Urls files are needed to be able to make http requests, so every url
has its own reference to a function in a views.py file. Project urls.py file has links to
application urls files, so it can be used by a user after all.

models.py contains settings for making migrations. In other words it contains instructions
for creating database, setting up and validate income information for a database.

serializers.py contains instructions for the process of translating a data structure
or object state into a format that can be stored or transmitted and reconstructed later.
