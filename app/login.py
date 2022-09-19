from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror
from app.functionality import routing
from app.functionality import validate
from app.store import state, states
import os, requests, json

def load_login(window):
    # Creating the login frame    
    frame=Frame(window, width=1366, height=768, bg='#111111')
    frame.place(x=0, y=0)


    # Creating the canvas
    login_canvas = Canvas(
        window,
        bg = "#111111",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    login_canvas.place(x = 0, y = 0)


    def submit():
        try:
            # Storing the values from the entry fields
            email = email_entry.get()
            password = password_entry.get();
            condition = validate.validate_login(email, password)

            # If validation fails
            if condition['status'] != 'success':
                showwarning('Error', condition['message'])
            else:
                # Get the name and the password from the database
                response = requests.post(os.getenv('BACKEND_URL_DEVELOPMENT')+'/api/login', json={'email': email, 'password': password})
                # throwing exception in case of api error
                response.raise_for_status()
                # converting the response from json to python dictionary
                data = json.loads(response.text)
                # checking if the user was created
                if data['status'] == 'success':
                    showinfo('Success', data['message'])
                    # storing the user id in the state
                    state.set_state(states.USERNAME, data['payload']['name'])
                    # loading the dashboard page
                    routing.route_frame(window, 'home')
                if data['status'] == 'error':
                    showwarning('Error', data['message'])
        except Exception as e:
            print(e)
            showerror('Error', 'An error has occurred.')

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
        command = submit,
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

    email_entry.insert(0, "tester@tester.com");
    password_entry.insert(0, "tester")
