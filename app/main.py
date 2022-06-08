from tkinter import *
from tkinter.messagebox import showerror
from app.login import load_login
from app.common import center, dark_title_bar
from app.functionality import weatherapi 

class MainWindow():
    def __init__(self):
        # window configuration
        window = Tk()
        window.geometry("1366x768")
        window.title('ForgePDF')
        window.configure(bg = "#111111")
        center(window)

        # calling the weather api and storing the JSON object in tthe json file
        weatherapi.getWeatherData()

        # Call the loadLogIn function to load the login screen
        load_login(window)
        # Additional window config
        window.resizable(False, False)
        window.iconbitmap('images/logo.ico')
        window.deiconify()
        dark_title_bar(window)
        window.mainloop()
