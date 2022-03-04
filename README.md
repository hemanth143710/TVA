# TVA

Django REST framework is a powerful and flexible toolkit for building Web APIs.

Requirements
    Python 3.6
    Django 3.1
    Django REST Framework

Installation

After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command

$ python -m venv env

After this, it is necessary to activate the virtual environment.

First, we have to start up Django's development server.

$ python manage.py runserver

Commands:-

Get all Details
http http://127.0.0.1:8000/api/User

Get a single Detail
http GET http://127.0.0.1:8000/api/User/<int:id>

Create
http POST http://127.0.0.1:8000/api/User

Update 
http PUT http://127.0.0.1:8000/api/User/<int:id>

Delete a movie
http DELETE http://127.0.0.1:8000/api/User/<int:id>

Pagination:-

The API supports pagination, by default responses have a page_size=5 but if you want change that you can pass through params limit={your_page_size_number}


http://127.0.0.1:8000/api/User?page=2

http://127.0.0.1:8000/api/User?page=1&limit=3

Filters:-

The API supports filtering, you can filter by the attributes of a details like this

http://127.0.0.1:8000/api/User?page=1&limit=3&sort=-age

http://127.0.0.1:8000/api/User?page=1&limit=3&name=le





