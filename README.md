# BigWordsNew

New backend for BigWords. Flask application with a sqlite database.

# Setup

### Windows (Powershell):

Install dependencies:

```
> py -3 -m venv venv
> pip3 install -r requirements.txt
```

To configure the environment and run the app:

```
> $env:FLASK_APP = "flaskr"
> $env:FLASK_ENV = "development"
> flask run
```
### Mac:

Install dependencies:

```
$ python3 -m venv venv
$ pip3 install -r requirements.txt
```

To configure the environment and run the app:

```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```