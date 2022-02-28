## CSV File to Database Data Import using Django Models and Custom Commands
Comma separated value is a standard format for importing and exporting data from spreadsheets to databases. 

This project demonstrates how to import users data from a csv file into a db using Django. 
The first row in the csv file is the headings row for the column names in a spreadsheet. 
The other rows in the csv represent each row on the spreadsheet with each of the column entries separated by a comma.


The database field names are defined in the models.py Django app file. 
This represents each column from the csv file as well. 
The commented commands are run to create and store the models table in the db and create a superuser on Django admin. 


A view for the models on the Django admin site is defined on the admin.py file.

Create a Django custom command for importing the data from the csv file. 
Instructions for the structuring the command files can be found here https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/ . 
The csv file is imported on line 8 of csv_import.py . 
DictReader allows the information on each row to be mapped to a header name as a key.

When the custom django command is run, the data from the csv file is imported into the Django database. 
This can be seen on the Django admin site
