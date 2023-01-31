from tkinter import *
from app.utility import center, dark_title_bar
from app.functionality import routing
import os

class MainWindow():
    def __init__(self):
        # window configuration
        window = Tk()
        window.geometry("1366x768")
        window.title('ForgePDF')
        window.configure(bg = "#111111")
        center(window)

        # Call the home frame
        routing.route_frame(window, 'home')
        # Additional window config
        window.resizable(False, False)
        window.iconbitmap(os.getenv('IMAGE_FOLDER_PATH')+'/logo.ico')
        window.deiconify()
        dark_title_bar(window)
        window.mainloop()
