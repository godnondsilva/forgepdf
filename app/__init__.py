# from app import main

from tkinter import *
from tkinter.messagebox import showerror
from app.login import load_login
from app.utility import center, dark_title_bar

class MainWindow():
    def __init__(self):
        # window configuration
        window = Tk()
        window.geometry("1366x768")
        window.title('ForgePDF')
        window.configure(bg = "#111111")
        center(window)

        # Call the loadLogIn function to load the login screen
        load_login(window)
        # Additional window config
        window.resizable(False, False)
        window.iconbitmap('images/logo.ico')
        window.deiconify()
        dark_title_bar(window)
        window.mainloop()


def run():
    MainWindow()