from django.core.management.base import BaseCommand
from csvimportdemo import models
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        csv_file = open('employee_data.csv', 'r')
        reader = csv.DictReader(csv_file)

        for row in reader:
            employee = models.Employees( email=row['Login email'],
                                         employee_id=row['Identifier'],
                                         first_name=row['First name'],
                                         last_name=row['Last name'])
            employee.save()

# run python manage.py csv_import run this script
