from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror

from app import register, home
import mysql.connector
from app import store
from app.functionality import validate
from app.store import state
import os

def load_login(window):
     # Button functions 
    def route_register():
        # call the load_register function to swap the frame to register screen
        register.load_register(window)

    def submit_details():
        try:
            # storing the values from the entry fields
            email = email_tbox.get()
            password = password_tbox.get();
            condition = validate.validate_login(email, password)
            if condition != True:
                showwarning('Error', condition['error'])
            else:
                # creating a mysql connection
                mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
                mycursor = mydb.cursor()
                # getting all the user data from the database
                mycursor.execute("select name, password, user_id from users where email='" + email + "'")
                # selecting only the first row from the fetched data
                result = mycursor.fetchone()
                print(result)

                # checking if the 'name' exists in the database
                if result == None:
                    showwarning('Error', 'Email not found.')
                # checking if the 'password' matches the one in the database
                elif password != result[1]:
                    showwarning('Error', 'Invalid Password!.')
                # else, successfull login
                else:
                    showinfo('Successfull', 'You have successfully logged in!')
                        # destroy the current window instance (SignUpWindow)
                    
                    #Stores the UID in a py file
                    state.set_uid(result[2])
                    state.set_username(result[0])
                    store.setUID(result[2])
                    store.setUsername(result[0])

                    # call the Home window class
                    home.load_home(window)
                mydb.close()
        except Exception as e:
            print(e)
            showerror('Error', 'An error has occurred.')
            
    
    frame=Frame(window, width=1366, height=768, bg='#111111')
    frame.place(x=0, y=0)

    # Creating a Canvas and setting its configuration
    login_canvas = Canvas(
        window,
        bg = "#111111",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    login_canvas.place(x = 0, y = 0)

    # Background image
    background_img = PhotoImage(file = f"./images/login/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = login_canvas.create_image(
        671.0, 384.0,
        image=background_img)

    # Login button
    login_btn_img = PhotoImage(file = f"./images/login/login_btn.png")
    login_btn_label = Label(image=login_btn_img)
    login_btn_label.image = login_btn_img
    login_btn = Button(
        login_canvas,
        image = login_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = submit_details,
        relief = "flat")

    login_btn.place(
        x = 633, y = 481,
        width = 160,
        height = 51)

    # Email entry field
    email_tbox_img = PhotoImage(file = f"./images/login/tbox.png")
    email_tbox_bg = login_canvas.create_image(
        807.0, 429.5,
        image = email_tbox_img)

    email_tbox = Entry(
        bd = 0,
        font=16,
        fg= "#eeeeee",
        bg = "#333333",
        insertbackground= "#eeeeee",
        highlightthickness = 0)

    email_tbox.place(
        x = 641, y = 311,
        width = 331,
        height = 35)

    # Password entry field
    password_tbox_img = PhotoImage(file = f"./images/login/tbox.png")
    password_tbox_bg = login_canvas.create_image(
        807.0, 329.5,
        image = password_tbox_img)

    password_tbox = Entry(
        bd = 0,
        font=16,
        fg= "#eeeeee",
        bg = "#333333",
        insertbackground= "#eeeeee",
        show="*",
        highlightthickness = 0)

    password_tbox.place(
        x = 641, y = 411,
        width = 331,
        height = 35)

    # Register button
    register_btn_img = PhotoImage(file = f"./images/login/register_btn.png")
    register_btn_label = Label(image=register_btn_img)
    register_btn_label.image = register_btn_img
    register_btn = Button(
        login_canvas,
        image = register_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = route_register,
        relief = "flat")

    register_btn.place(
        x = 1131, y = 41,
        width = 142,
        height = 41)
