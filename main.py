from pkg_resources import require
import sys,os
import app

from tkinter import *
from app.main import MainWindow

if len(sys.argv) > 1 and '--dev' in sys.argv:
    print("INFO: --dev option is specified. Running in development mode.")
    os.environ["IMAGE_FOLDER_PATH"] = "dist/images"
else:
    print("WARN: --dev option is not specified. Running in production mode.")
    os.environ["IMAGE_FOLDER_PATH"] = "images"

def run():
    MainWindow()

if __name__ == '__main__':
    try:
        run()
    # Catching the error if the user tries to run the app without using the proper image directory
    except TclError:
        print("ERROR: Application found running in development mode without --dev option.")
        print("INFO: Please add the --dev option")