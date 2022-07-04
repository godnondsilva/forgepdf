# This file contains all the common functions used
# across the application

import mysql.connector
import os
import ctypes as ct

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
def execute_query(query):
    mydb = mysql.connector.connect(host=os.getenv('HOST'),user=os.getenv('USER'),password=os.getenv('PASSWORD'),database="forgepdf")
    mycursor=mydb.cursor()
    mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()

# This exportable function is used to execute
# a query and return one row from the cursor
def execute_query_fetch_one(query):
    mydb = mysql.connector.connect(host=os.getenv('HOST'),user=os.getenv('USER'),password=os.getenv('PASSWORD'),database="forgepdf")
    mycursor=mydb.cursor()
    mycursor.execute(query)
    result=mycursor.fetchone()
    mycursor.close()
    mydb.close()
    return result

# This exportable function is used to execute
# queries and return the all the rows from the cursor
def execute_query_fetch_all(query):
    mydb = mysql.connector.connect(host=os.getenv('HOST'),user=os.getenv('USER'),password=os.getenv('PASSWORD'),database="forgepdf")
    mycursor=mydb.cursor()
    mycursor.execute(query)
    result=mycursor
    # mycursor.close()
    # mydb.close()
    return mycursor

# This exportable function is used to update the 
# title bar to dark theme
def dark_title_bar(window):
    """
    MORE INFO:
    https://docs.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))