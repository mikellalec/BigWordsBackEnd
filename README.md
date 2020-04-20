# BigWordsNew

New backend for BigWords. Flask application with a sqlite database.

# Setup

Create a folder at the root directory called "data" and copy into the folder the Big Words data from the Dropbox: https://www.dropbox.com/sh/oagd0pngqwlimy6/AAAsdGfO2En_w5owPniE7rOta?dl=0

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
# Test

 Run the app and navigate to http://localhost:5000/