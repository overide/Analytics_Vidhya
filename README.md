# Analytics_Vidhya
This is my project for web developer intern challenge @ Analytics Vidhya

## Project
analytics

## Applications
* recruiter - Handles Recruiter for search and filter database 
* accounts - Handles Authentication and Authorization

## Database
* Postgresql

## Project Deployment
Before running the project first setup your database. Add following as **default** to the **DATABASE** field in **settings.py**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'applicant',
        'USER': 'overide',
        'PASSWORD': 'applicant',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
Now make migrations by following commands
```
python manage.py makemigrations
```
Let's migrate

```
python manage.py migrate
```
Now start the localserver to run the project
```
python manage.py runserver
```
This will start your local server @ **127.0.0.1:8000**

Database modification privilage is provided to Admin only so create a **superuser**
```
python manage.py createsuperuser
```
For adding entries to database login to Admin from the access link provided by Admin button at homepage or this link **127.0.0.1:8000/admin**
After successfull login, you can add entries to **Applicant** 

## Populating database

**recruiter.json** file contains some test records which can be used to populate the database for testing recruiter panel.Use following command to load data in database
```
python manage.py loaddata recruiter.json
```
## Note
In **setting.py** set **DEBUG** field to **False** if you want to deploy project on production. 
