# DRF test

`python3 -m venv venv`

`. venv/bin/activate`

`pip install -U pip`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py runserver`

Go to http://localhost:8000/admin/restaurant/

Make some foods and categories.

Go to http://localhost:8000/api/v1/foods/?format=api
