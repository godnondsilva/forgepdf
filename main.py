from pkg_resources import require
import sys,os
import app

# Initializing dotenv to read the .env file
from dotenv import load_dotenv, find_dotenv
from tkinter import *
from app.main import MainWindow
load_dotenv(find_dotenv())

if len(sys.argv)==2 and sys.argv[1]=='--dev':
    print("INFO: --dev option is specified. Running in development mode.")
    os.environ["IMAGE_FOLDER_PATH"] = os.getenv("IMAGE_FOLDER_PATH_DEVELOPMENT")
else:
    print("WARN: --dev option is not specified. Running in production mode.")
    os.environ["IMAGE_FOLDER_PATH"] = os.getenv("IMAGE_FOLDER_PATH_DEPLOYMENT")

def run():
    MainWindow()

if __name__ == '__main__':
    try:
        run()
    # Catching the error if the user tries to run the app without using the proper image directory
    except TclError:
        print("ERROR: Application found running in development mode without --dev option.")
        print("INFO: Please add the --dev option")