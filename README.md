# ForgePDF

A PDF editor application for windows using Tkinter and Python.

# Documentation

## Initial setup

- Install python virtual environment package if not installed already `pip install virtualenv`.
- Create a python virtual environment `virtualenv <environment_name>`.
- Run the virtual environment:
  - For windows based systems (environment_name): `source <environment_name>\Scripts\activate.bat`.
  - For Unix based systems (environment_name): `source <environment_name>/bin/activate`.
- Install dependencies `pip install -r requirements.txt`.

## Running frontend in development mode

- Run the project `py main.py --dev` [--dev option must be specified].

## Building the project

- Install pyinstaller `pip install pyinstaller`
- Create initial build `pyinstaller --onefile -w -i dist/logo.ico`.
- Update the project build `pyinstaller main.spec`.

## Running frontend in production mode & packaging

- The file `ForgePDF.exe` file will execute the application.
- Package together along the dist folder and you can share the application.
