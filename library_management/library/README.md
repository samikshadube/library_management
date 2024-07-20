# LIBRARY_MANAGEMENT

This is a django task for managing library system.
Admins can manage books,authors and borrow record.
This application allow admin to add books ,authors and assign book to authors.Additionally admin can export data to excel sheet.

## Features

- Manage Authors: Add, update, and delete author information.
- Manage Books: Add, update, and delete book information.
- Manage Borrow Records: Add, update, and delete borrow records.
- Export Data: Export authors, books, and borrow records to separate sheets in an Excel file.
- Pagination: Paginated lists of authors, books, and borrow records.

## Requirements

- Python 3.x
- Django 3.x or later
- OpenPyXL (for exporting to Excel)

### Note:

- Here I used Library Openpyxl (for exporting to excel) instead of Django-excel because I was facing some issues in this library.

## Installation

Git Clone the repository


## Apply Migrations Step

Run the command in terminal 
- python manage.py makemigrations

then 
- python manage.py migrate

## To Create a SuperUser

- python manage.py createsuperuser

### To use already created Superuser, ceredentials are:
- username - samiksha
- password - 1212345

## To Run the Development Server

- python manage.py runserver

## To Access the Application 

- On Web Browser go to 'http://127.0.0.1:8000'