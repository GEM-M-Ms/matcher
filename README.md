# GEM Matcher Service

## Introduction

## Development

The GEM Matcher Service is a [`django`](https://www.djangoproject.com/) web application hosted on [`heroku`](https://www.heroku.com/).

### Local Development

#### Installing dependecies

To run locally install [Python](https://www.python.org/) and then install [`Pipenv`](https://github.com/pypa/pipenv) using `pip install pipenv`.

Once installed run `pipenv sync --dev` in the root directory to install the project dependencies.

#### Database

To run [`Postgres`](https://www.postgresql.org/) locally simply install [`Docker`](https://docs.docker.com/get-docker/) and then run `docker-compose up` in the root directory.

#### Settings

Next create a file `matcher/local_settings.py` in the project and add the following configuration to connect to your running database:

```python
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': 'matcher',
      'USER': 'postgres',
      'PASSWORD': 'postgres',
      'HOST': 'localhost',
      'PORT': '5432',
  }
}
```

#### Running Django commands

Activate the project envrionment using `pipenv shell`.

Once the shell is activate the following commands should work:

- `python manage.py migrate` to create database tables.
- `python manage.py createsuperuser` to create an admin user.
- `python manage.py runserver` to run the local development server.

#### Reformatting code

You can reformat the code by running `black .` in the `matcher` directory.
