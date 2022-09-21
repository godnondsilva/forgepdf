# ForgePDF

A PDF editor application for windows using Tkinter and Flask.

# Frontend Documentation (Tkinter)

## Initial setup

- Install python virtual environment package if not installed already `pip install virtualenv`.
- Create a python virtual environment `virtualenv <environment_name>`.
- Run the virtual environment:
  - For windows based systems (environment_name): `source <environment_name>\Scripts\activate.bat`.
  - For Unix based systems (environment_name): `source <environment_name>/bin/activate`.
- Install dependencies `pip install -r requirements.txt`.

## Setting frontend environment variables

- Create a copy of .env.example to .env `cp .env.example .env`.
- For `BACKEND_URL`:
  - In local development, set the variable to `http://localhost:5000`.
  - In production development, set the variable to the published URL

## Running frontend in development mode

- Run the project `py main.py --dev` [--dev option must be specified].

## Building the project

- Install pyinstaller `pip install pyinstaller`
- Create initial build `pyinstaller --onefile -w -i dist/logo.ico`.
- Update the project build `pyinstaller main.spec`.

## Running frontend in production mode & packaging

- The file `ForgePDF.exe` file will execute the application.
- Package together the folder dist along with the .env file.

# Backend Documentation (Flask)

## Database setup

- Run the psql command using a termninal (Eg: Git bash)
- Login to your PSQL account `psql -U <user>`.
- Enter your password.
- Create the database `CREATE DATABASE forgepdf;`.
- Connect to that database `\c forgepdf;`.
- Create the necessary tables.
  - Using flask-migrate.
    - Run the command `flask db upgrade`
  - Using manual create table query.
    - Enter the following SQL query:
      ```
      create table "users" (
        user_id serial primary key,
        name varchar(30) not null,
        email varchar(30) not null,
        password varchar(30) not null
      );
      ```

## Backend setup

- Install python virtual environment package if not installed already `pip install virtualenv`.
- Create a python virtual environment `virtualenv <environment_name>`.
- Run the virtual environment:
  - For windows based systems (environment_name): `source <environment_name>\Scripts\activate.bat`.
  - For Unix based systems (environment_name): `source <environment_name>/bin/activate`.
- Install dependencies `pip install -r requirements.txt`

## Setting backend environment variables

- Create a copy of .env.example to .env `cp .env.example .env`.
- For `DATABASE_URL`:
  - In local development, set the variable to `postgresql://<username>:<password>@localhost:5432/forgepdf`.
  - In production development, set the variable to the published URL
- For `WEATHER_API_KEY`:
  - In local and production development, set the variable to your [OpenWeatherMap API key](https://openweathermap.org/)

## Running backend in development mode

- Run the backend `flask run`.

## Running backend in production mode

- Run the backend `gunicorn app:app`. <br />**Note:** This command works only on Linux.
