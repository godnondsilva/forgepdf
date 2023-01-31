from pkg_resources import require
import sys,os
import app

from tkinter import *
from app.main import MainWindow

# Backend URL for the application is an enviroment variable. 
# Change it to your deployed backend URL
BACKEND_URL = "https://forgepdf-backend.onrender.com"

if len(sys.argv) > 1 and '--dev' in sys.argv:
    print("INFO: --dev option is specified. Running in development mode.")
    os.environ["IMAGE_FOLDER_PATH"] = "dist/images"
else:
    print("WARN: --dev option is not specified. Running in production mode.")
    os.environ["IMAGE_FOLDER_PATH"] = "images"

if len(sys.argv)==3 and '--dev' in sys.argv[1] and '--local' in sys.argv:
    print("INFO: --local option is specified. Running development backend.")
    os.environ["BACKEND_URL"] = "http://localhost:5000"
else:
    print("WARN: --local option is not specified. Running production backend.")
    os.environ["BACKEND_URL"] = BACKEND_URL

def run():
    MainWindow()

if __name__ == '__main__':
    try:
        run()
    # Catching the error if the user tries to run the app without using the proper image directory
    except TclError:
        print("ERROR: Application found running in development mode without --dev option.")
        print("INFO: Please add the --dev option")