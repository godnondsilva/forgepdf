# This file contains all the common functions used
# across the application

import mysql.connector
import os

# This exportable function is used to display 
# the window at the center of the page
def center(window):
    app_width=1366 
    app_height=768
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x=(screen_width / 2) - (app_width/2)
    y=(screen_height / 2) - (app_height/2)
    window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

# This exportable function is used to execute 
# queries passed as a parameter
def executeQuery(query):
    mydb = mysql.connector.connect(host=os.getenv('HOST'),user=os.getenv('USER'),password=os.getenv('PASSWORD'),database="forgepdf")
    mycursor=mydb.cursor()
    mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()