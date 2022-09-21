<h1>Here is a REST API for Car park.</h1></p></p>


## API

[📚 Documentation 📚](https://documenter.getpostman.com/view/22115905/2s7Z7cmCfz)

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

_________________________________________________________________________________________________________________________________



## Dependencies
Use `[pipenv]` or `[pip]` to install dependencies:


### `[pipenv]`

The __Pipifile__ and __Pipfile.lock__ files contains info about project dependencies.
To install all dependencies form a __Pipifile__ the __pipenv__ package required.

Install the __pipenv__ package:
```
pip install pipenv
```

Once __pipenv__ is installed, 
the following command will create virtual enviroment and install all project dependencies:
```
pipenv install
```


### `[pip]`

To install all dependencies form a __requirements.txt__ file enter the following command:
```
pip install -r requirements.txt
```


## Enviroment Variables

For the server to run properly, the __.env__ file has to be created, which has to contain environment variables, such as:
* `SECRET_KEY=some-key`

## Starting the server

To start the server run:
```
python mange.py runserver
```

## Admin profile login data:

Username: admin
Password: admin
E-mail: admin@example.com

