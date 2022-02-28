from django.db import models

class Employees(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    employee_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.email

# run  python manage.py makemigrations <app name> when changes are made to the models
# run  python manage.py migrate
# run python manage.py createsuperuser to create a Django admin user
# run python manage.py runserver to run the app on your local machine
# visit http://127.0.0.1:8000/admin/ to view the admin site
