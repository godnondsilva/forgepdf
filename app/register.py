from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror
from app.functionality import routing
from app.functionality import validate
import os, requests, json

def load_register(window):
    register_frame=Frame(window, width=1366, height=768, bg='#111111')
    register_frame.place(x=0, y=0)


    register_canvas = Canvas(
        register_frame,
        bg = "#111111",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    register_canvas.place(x = 0, y = 0)


    def submit():
        try:
            # storing the values from the entry fields
            name = name_entry.get()
            email = email_entry.get()
            password = password_entry.get()

            # validating the details
            condition = validate.validate_register(name, email, password)
            # if validation fails
            if condition['status'] == 'error':
                showwarning('Error', condition['error'])
            else:
                showinfo('Notice', "Registering... Please wait")
                # Insert the new user into the database
                response = requests.post(os.getenv('BACKEND_URL_DEVELOPMENT')+'/api/register', json={'name': name, 'email': email, 'password': password})
                # throwing exception in case of api error
                response.raise_for_status()
                # converting the response from json to python dictionary
                data = json.loads(response.text)
                # checking if the user was created
                if data['status'] == 'success':
                    showinfo('Success', data['message'])
                    # clearing the entry fields
                    name_entry.delete(0, END)
                    email_entry.delete(0, END)
                    password_entry.delete(0, END)
                    # loading the login page
                    routing.route_frame(window, 'login')
                else:
                    showerror('Error', 'An error has occurred.')
        except Exception as e:
            print(e)
            showerror('Error', 'An error has occurred.')
    

    background_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/register/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = register_canvas.create_image(
        671.0, 384.0,
        image=background_img)


    login_label_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/register/login_btn.png")
    login_btn_label = Label(image=login_label_img)
    login_btn_label.image = login_label_img
    login_btn = Button(
        image = login_label_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = lambda: routing.route_frame(window, "login"),
        relief = "flat")
    login_btn.place(
        x = 1131, y = 41,
        width = 142,
        height = 41)
    
    
    name_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/register/entry.png")
    name_entry_bg = register_canvas.create_image(
        807.0, 527.5,
        image = name_entry_img)
    name_entry = Entry(
        bd = 0,
        font=16,
        fg= "#eeeeee",
        bg = "#333333",
        insertbackground= "#eeeeee",
        highlightthickness = 0)
    name_entry.place(
        x = 641, y = 310,
        width = 331,
        height = 35)


    email_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/register/entry.png")
    email_entry_bg = register_canvas.create_image(
        807.0, 427.5,
        image = email_entry_img)
    email_entry = Entry(
        bd = 0,
        font=16,
        fg= "#eeeeee",
        bg = "#333333",
        insertbackground= "#eeeeee",
        highlightthickness = 0)
    email_entry.place(
        x = 641, y = 410,
        width = 331,
        height = 35)


    password_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/register/entry.png")
    password_entry_bg = register_canvas.create_image(
        807.0, 328.5,
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
        x = 641, y = 510,
        width = 331,
        height = 35)


    register_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/register/register_btn.png")
    register_btn_label = Label(image=register_img)
    register_btn_label.image = register_img
    register_btn = Button(
        image = register_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = submit,
        background="#111111",
        activebackground="#111111",
        relief = "flat")
    register_btn.place(
        x = 633, y = 576,
        width = 160,
        height = 51)

