from tkinter import *
from app.store import state, states
from app.functionality import routing
import os

def load_sidebar(window):
    # Router guard 
    # Reset selected pdf and selected pdfs when changing the frame
    state.set_state(states.SELECTED_PDF, '')
    state.set_state(states.SELECTED_PDFS, [])


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
        command = lambda: routing.route_frame(window, "home"),
        relief = "flat")
    home_btn.place(
        x = 48, y = 180,
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
        command = lambda: routing.route_frame(window, "encryptpdf"),
        relief = "flat")
    encrypt_btn.place(
        x = 48, y = 215,
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
        command = lambda: routing.route_frame(window, "decryptpdf"),
        relief = "flat")
    decrypt_btn.place(
        x = 48, y = 250,
        width = 108,
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
        command = lambda: routing.route_frame(window, "splitpdf"),
        relief = "flat")
    split_btn.place(
        x = 48, y = 285,
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
        command = lambda: routing.route_frame(window, "mergepdf"),
        relief = "flat")
    merge_btn.place(
        x = 48, y = 320,
        width = 94,
        height = 27)