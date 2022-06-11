from tkinter import *
from tkinter.messagebox import showwarning, showerror, showinfo
import mysql.connector
from app import login
from app.functionality import validate
from app.utility import executeQuery
import os

def load_register(window):
        # Button functions
    def route_login():
        # call the load_login function to swap the frame to login screen
        login.load_login(window)

    def submit_details():
        try:
            # storing the values from the entry fields
            name = name_tbox.get()
            email = email_tbox.get()
            password = password_tbox.get()

            condition = validate.validate_register(name, email, password)
            if condition != True:
                showwarning('Error', condition['error'])
            else:
                # creating a query and checking if there exist a account before signing up
                mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
                mycursor = mydb.cursor()
                # getting all the user data from the database
                mycursor.execute("select name, password from users where name='" + name + "'")
                # selecting only the first row from the fetched data
                result = mycursor.fetchone()
                    
                # creating a query to insert the user details into the database
                query = "insert into users (name, email, password) values('" + name + "','" + email + "','" + password + "')"
                executeQuery(query)

                # TODO: Display status message (success/failure)
                if result == None:
                    showinfo('Successfull','You have successfully registered an account! Please login to continue!')
                    # call the Home window class
                    login.load_login(window)

                elif result != None:
                    showwarning("Error" , "A user with this name already exist, please choose a new one!")
        except:
            showerror('Error', 'An error has occurred.')
    

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

    background_img = PhotoImage(file = f"./images/register/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = register_canvas.create_image(
        671.0, 384.0,
        image=background_img)

    login_label_img = PhotoImage(file = f"./images/register/login_btn.png")
    login_btn_label = Label(image=login_label_img)
    login_btn_label.image = login_label_img
    login_btn = Button(
        register_canvas,
        image = login_label_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = route_login,
        relief = "flat")

    login_btn.place(
        x = 1131, y = 41,
        width = 142,
        height = 41)
    
    name_tbox_img = PhotoImage(file = f"./images/register/tbox.png")
    name_tbox_bg = register_canvas.create_image(
        807.0, 527.5,
        image = name_tbox_img)
    
    name_tbox = Entry(
        bd = 0,
        font=16,
        fg= "#eeeeee",
        bg = "#333333",
        insertbackground= "#eeeeee",
        highlightthickness = 0)

    name_tbox.place(
        x = 641, y = 310,
        width = 331,
        height = 35)

    email_tbox_img = PhotoImage(file = f"./images/register/tbox.png")
    email_tbox_bg = register_canvas.create_image(
        807.0, 427.5,
        image = email_tbox_img)

    email_tbox = Entry(
        bd = 0,
        font=16,
        fg= "#eeeeee",
        bg = "#333333",
        insertbackground= "#eeeeee",
        highlightthickness = 0)

    email_tbox.place(
        x = 641, y = 410,
        width = 331,
        height = 35)

    password_tbox_img = PhotoImage(file = f"./images/register/tbox.png")
    password_tbox_bg = register_canvas.create_image(
        807.0, 328.5,
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
        x = 641, y = 510,
        width = 331,
        height = 35)

    register_img = PhotoImage(file = f"./images/register/register_btn.png")
    register_btn_label = Label(image=register_img)
    register_btn_label.image = register_img
    register_btn = Button(
        register_canvas,
        image = register_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = submit_details,
        background="#111111",
        activebackground="#111111",
        relief = "flat")

    register_btn.place(
        x = 633, y = 576,
        width = 160,
        height = 51)

