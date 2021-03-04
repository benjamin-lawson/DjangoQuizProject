# Django Quiz App

## Description
This application was made as a RESTful quiz website built on top of the Django Framework.

## Getting Started

### Installation
**Open a PowerShell window**

I suggest PowerShell for Windows, but you can use whatever CLI that you feel comfortable with.

**Pull the most recent release** 

```
git clone git@github.com:benjamin-lawson/DjangoQuizProject.git
```

**Navigate to the project directory** 

```
cd DjangoQuizProject
```

**Create a virtual environment** 

```
python -m virtualenv venv
```
*NOTE: If you do not have the virtual environment library installed, you can install it via `python -m pip install virtualenv`*

**Activate the virtual environment** 

```
./venv/Scripts/activate
```

**Install the required libraries** 

```
python -m pip install -r requirements.txt
```

**Create the database structure** 

```
python manage.py migrate
```

**Create the admin account**

```
python manage.py createsuperuser
```

**Run the server locally**

```
python manage.py runserver 8000
```

### Documentation
Once the server is running without errors, you can access the 
[Swagger UI](localhost:8000/schema/swagger-ui) or [Redoc](localhost:8000/schema/swagger-ui) documentation.
These pages will give you an outline of how to interact with the API.

### Authentication
This web server utilizes the JWT standard for authentication into our API. To get started, pass a username and password 
to [localhost:8000/auth/](localhost:8000/auth/).