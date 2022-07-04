# ForgePDF

A PDF editor application for windows using Python and Tkinter

# Documentation

## Initial setup

- [OPTIONAL] Install python virtual environment package `pip install virtualenv`.
- Create a python virtual environment `virtualenv <environment_name/environment_name>`.
- Run the virtual environment:
  - For windows based systems (environment_name): `source <environment_name>\Scripts\activate.bat`
  - For Unix based systems (environment_name): `source <environment_name>/bin/activate`
- Install dependencies `pip install -r requirements.txt`.

## Development mode

- Run the project locally `py main.py --dev` [--dev option must be specified].

## Build project

- Install pyinstaller `pip install pyinstaller`
- Create initial build `pyinstaller --onefile -w -i dist/logo.ico`.
- Update the project build `pyinstaller main.spec`.

## Production mode

- Open the `ForgePDF.exe` file from the dist folder.
