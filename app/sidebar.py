from tkinter import *
from app import home, encryptpdf
import os

def load_sidebar(window):

    def route_home():
        home.load_home(window)

    def route_encypt_pdf():
        encryptpdf.load_encrypt_pdf(window)

    def btn_clicked():
        pass

    background_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/sidebar/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background_label.place(
        x = 0, y = 0,
        width = 245,
        height = 768)

    home_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/sidebar/home_btn.png")
    home_btn_label = Label(image=home_btn_img)
    home_btn_label.image = home_btn_img
    home_btn = Button(
        image = home_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = route_home,
        relief = "flat")

    home_btn.place(
        x = 48, y = 181,
        width = 54,
        height = 27)

    encrypt_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/sidebar/encrypt_btn.png")
    encrypt_btn_label = Label(image=encrypt_btn_img)
    encrypt_btn_label.image = encrypt_btn_img
    encrypt_btn = Button(
        image = encrypt_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = route_encypt_pdf,
        relief = "flat")

    encrypt_btn.place(
        x = 48, y = 222,
        width = 105,
        height = 27)

    decrypt_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/sidebar/decrypt_btn.png")
    decrypt_btn_label = Label(image=decrypt_btn_img)
    decrypt_btn_label.image = decrypt_btn_img
    decrypt_btn = Button(
        image = decrypt_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    decrypt_btn.place(
        x = 48, y = 256,
        width = 108,
        height = 27)

    email_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/sidebar/email_btn.png")
    email_btn_label = Label(image=email_btn_img)
    email_btn_label.image = email_btn_img
    email_btn = Button(
        image = email_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    email_btn.place(
        x = 48, y = 290,
        width = 86,
        height = 27)

    extract_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/sidebar/extract_btn.png")
    extract_btn_label = Label(image=extract_btn_img)
    extract_btn_label.image = extract_btn_img
    extract_btn = Button(
        image = extract_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    extract_btn.place(
        x = 48, y = 324,
        width = 98,
        height = 27)

    split_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/sidebar/split_btn.png")
    split_btn_label = Label(image=split_btn_img)
    split_btn_label.image = split_btn_img
    split_btn = Button(
        image = split_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    split_btn.place(
        x = 48, y = 358,
        width = 76,
        height = 27)

    merge_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/sidebar/merge_btn.png")
    merge_btn_label = Label(image=merge_btn_img)
    merge_btn_label.image = merge_btn_img
    merge_btn = Button(
        image = merge_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    merge_btn.place(
        x = 48, y = 388,
        width = 94,
        height = 27)