# Project Title
## Developer-Awards

## Author
[Esther-Anyona](https://github.com/Esther-Anyona)
<hr>

[Live link]()

## Description
This is a django web application of a clone of the website for the popular photo app Instagram


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
1. git clone the repository
    - https://github.com/esther-anyona/developer-awards.git
1. cd into app directory
    - cd developer-awards
1. create a virtual env
    -  python3 -m venv virtual
1. activate virtual environ
    - source virtual/bin/activate
1. Install all dependancies
1. Make Migrations
python3 manage.py makemigrations
    - Apply migrattions to database
    - python3 manage.py migrate
1. To run the app on localhost
    - python3 manage.py runserver

### Prerequisites

The application requires the following installations to operate:

* pip
* gunicorn
* django
* psycopg2

## Requirements
As a user I can perform the following functions:

- View posted projects and their details
- Post a project to be rated
- Rate/ review other users' projects
- Search for projects 
- View projects overall score
- View my profile page


## Creating .env

Required file to keep sensitive data that should not be exposed in github

SECRET_KEY = '<Secret_key>'

DBNAME = 'awards'

USER = '<Username>'

PASSWORD = '<password>'

DEBUG = True

EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_HOST_USER = '<your-email>'

EMAIL_HOST_PASSWORD = '<your-password>'



## Running the tests

To run tests for this application in development:
1. run python3 manage.py test

## Deployment

Install heroku CLI to deploy on heroku
* Add a Procfile in the project root;
* Add requirements.txt file with all the requirements in the project root;
* Add Gunicorn to requirements.txt;
* A runtime.txt to specify the correct Python version in the project root;
* Configure whitenoise to serve static files.

## Built With
* Python3.8
* Django==4.0.2
* Bootstrap v5
* postgresql
* Heroku

## Authors
This was a solo project.

## Bugs
There are no known bugs at the moment but should you spot one, feel free to create a pull request.

## Contacts
You can reach me through:
* Email: jkemuntoe@gmail.com or
* Phone: +254724374477

## License
*MIT License*:
Copyright (c) 2022 *Esther Anyona*
