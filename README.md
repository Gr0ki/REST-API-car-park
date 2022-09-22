<h1>Here is a REST API for Car park.</h1></p></p>


## API

[📚 Documentation 📚](https://documenter.getpostman.com/view/22115905/2s7Z7cmCfz)


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

