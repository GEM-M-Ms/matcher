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

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

#### Running Django commands

Activate the project envrionment using `pipenv shell`.

Once the shell is activate the following commands should work:

- `python manage.py migrate` to create database tables.
- `python manage.py createsuperuser` to create an admin user.
- `python manage.py runserver` to run the local development server.

#### Reformatting code

You can reformat the code by running `black .` in the `matcher` directory.

### Setting email instructions
#### setup MailGun account

#### When use free domain sandbox13beb5d9b86648e887d7484dd54ca0d4.mailgun.org
     add emails as trusted in dashboard https://app.mailgun.com/app/dashboard
     
#### Oherwise create own subdomain

#### Add settings as appropriate

    EMAIL_BACKEND = "django_mailgun.MailgunBackend"
    MAILGUN_ACCESS_KEY = '...'
    MAILGUN_SERVER_NAME = '...'
    DEFAULT_FROM_EMAIL ='...'

#### Criteria Settings And Comparison

Criteria should exist prior to creating any match for the cohort. Criteria consists from mentee column name, Mentor Column Name, and weight .
Where weight is a ratio between 0.1 - 1.0. 
Criretia used for comparison testing was:
```
('Career','Current Industry', 1.),
  ('Hobbies', 'Hobbies', 0.5),
  ('Barriers', 'Barriers', 0.5),
  ('Describe Self','Describe Self',0.5),
  ('City/Town (City of Toronto, Durham, Halton, Peel, York)','Town',0.2),
  ('Ethnicity','Ethnicity',0.1),
  ('Religion', 'Religion', 0.1),

```

For every columnc match (eg 'Barriers' - 'Barriers'), ratio of text difference is calculated (0-100%). Then ratio is multiplied by weight ratio
```aidl
mentor_ratio_for_the_column=ratio*weight
```

Then average of all ratios is calculated for the mentor - all ratios are summed up and divided in the number of raws in criteria:

```aidl
mentor_ratio = mentor_ratio/number_of_raws_in_criteria_table
```
Therefore, when adding criteria setting, pls enter weight value as 0<weight <1.0
If 0 added, ratio would be 0 and result wont be valid.

#####Note on text difference comparison

For cases when both columns are just one string (like Cit-Town - no one can live in 2 towns in the same time), we use standard fuzzywuzzy string comparison package  fuzzy ,
refer to  examples/details - https://towardsdatascience.com/string-matching-with-fuzzywuzzy-e982c61f8a84
```aidl
ratio=fuzz.token_set_ratio(mentorValue,menteeValue)
```
This Function takes out common tokens prior calculating matching ratio.

However, there are cases where Mentee response is more than one option, however mentor does have just one response. Example is Career Industry:
```aidl
 if type(mentorValue) == 'str' and type(menteeValue) == 'list'
```
For such case we search mentor response in mentee answer. If included - ratio will be 
```
ratio=100*weight
 ```
 Otherwise
 ```
 ratio=0*weight
 ```
