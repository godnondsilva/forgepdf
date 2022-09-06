from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror
from app.functionality import routing

from app.functionality import validate
from app.store import state, states
from app.utility import execute_query_fetch_one
import os


def load_login(window):

    def submit_details():
        try:
            # storing the values from the entry fields
            email = email_entry.get()
            password = password_entry.get();
            condition = validate.validate_login(email, password)
            # if validation fails
            if condition != True:
                showwarning('Error', condition['error'])
            else:
                # Get the name and the password from the database
                result = execute_query_fetch_one("select name, password, user_id from users where email='" + email + "'")

                # checking if the 'email' exists in the database
                if result == None:
                    showwarning('Error', 'Email not found.')
                # checking if the 'password' matches the one in the database
                elif password != result[1]:
                    showwarning('Error', 'Invalid Password!.')
                # else, successfull login
                else:
                    showinfo('Successfull', 'You have successfully logged in!')
                    # Set the UID and the name in the state variable
                    state.set_state(states.UID, result[2])
                    state.set_state(states.USERNAME, result[0])
                    # call the Home window class
                    routing.route_frame(window, "home")
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
    background_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/login/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = login_canvas.create_image(
        671.0, 384.0,
        image=background_img)

    # Login button
    login_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/login/login_btn.png")
    login_btn_label = Label(image=login_btn_img)
    login_btn_label.image = login_btn_img
    login_btn = Button(
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
    email_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/login/entry.png")
    email_entry_bg = login_canvas.create_image(
        807.0, 429.5,
        image = email_entry_img)

    email_entry = Entry(
        bd = 0,
        font=16,
        fg= "#eeeeee",
        bg = "#333333",
        insertbackground= "#eeeeee",
        highlightthickness = 0)

    email_entry.place(
        x = 641, y = 311,
        width = 331,
        height = 35)

    # Password entry field
    password_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/login/entry.png")
    password_entry_bg = login_canvas.create_image(
        807.0, 329.5,
        image = password_entry_img)

    password_entry = Entry(
        bd = 0,
        font=16,
        fg= "#eeeeee",
        bg = "#333333",
        insertbackground= "#eeeeee",
        show="*",
        highlightthickness = 0)

    password_entry.place(
        x = 641, y = 411,
        width = 331,
        height = 35)

    # Register button
    register_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/login/register_btn.png")
    register_btn_label = Label(image=register_btn_img)
    register_btn_label.image = register_btn_img
    register_btn = Button(
        image = register_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = lambda: routing.route_frame(window, "register"),
        relief = "flat")

    register_btn.place(
        x = 1131, y = 41,
        width = 142,
        height = 41)

    email_entry.insert(0, "testing@testing.com");
    password_entry.insert(0, "something")
