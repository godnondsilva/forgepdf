from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo, showwarning, showerror
from app import sidebar
from app.store import state, states
from app.functionality import encrypt, validate
from app.utility import file_handler
import os

def load_encrypt_pdf(window):
    canvas = Canvas(
        window,
        bg = "#111111",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    sidebar.load_sidebar(window)

    def get_pdf():
        if state.get_state(states.SELECTED_PDF) != '':
            selected_pdf_entry.insert('0' , '')
            state.set_state(states.SELECTED_PDF, '')
        pdf_path = filedialog.askopenfilename(initialdir=os.getenv("DEFAULT_SAVE_FOLDER"), title="Select a file" , filetypes=(("Pdf files","*.pdf*"),("all files","*.*")))
        filename = os.path.basename(pdf_path)
        if len(pdf_path) == 0:
            showwarning("Error" , "Please select a PDF file")
            return
        show_preview_pdf(filename, pdf_path)

    def encrypt_pdf():
        password = encrypt_password_entry.get().strip()
        try:
            condition = validate.validate_encrypt(password)
            if condition['status'] == 'error':
                showwarning('Error', condition['message'])
            else:
                condition = encrypt.encrypt(state.get_state(states.SELECTED_PDF), password)
                if condition['status'] == 'success':
                    file_handler.move_to_downloads('encrypted')
                    showinfo('Success', condition['message'])
                else:
                    showwarning('Error', "An error has occurred")
        except Exception as e:
            print(e)
            showerror("Error" , "An error has occurred")


    def show_preview_pdf(filename, pdf_path):
        selected_pdf_entry.insert('0' , filename)
        state.set_state(states.SELECTED_PDF, pdf_path)
        selected_pdf_btn.place(
            x = 1082, y = 248,
            width = 137,
            height = 159)
        selected_pdf_entry.place(
            x = 1101, y = 374,
            width = 101,
            height = 13)
    
    background_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/encryptpdf/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = canvas.create_image(
        682.0, 384.0,
        image=background_img)


    selected_pdf_btn_image = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/encryptpdf/selected_pdf_btn.png")
    selected_pdf_btn_label = Label(image=selected_pdf_btn_image)
    selected_pdf_btn_label.image = selected_pdf_btn_image
    selected_pdf_btn = Button(
        image = selected_pdf_btn_image,
        borderwidth = 0,
        highlightthickness = 0,
        background="#5a5a5a",
        activebackground="#5a5a5a",
        relief = "flat")

    selected_pdf_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/encryptpdf/selected_pdf_entry.png")
    selected_pdf_bg = canvas.create_image(
        1151.5, 381.5,
        image = selected_pdf_entry_img)
    selected_pdf_entry = Entry(
        bd = 0,
        font=("Poppins", 8),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#5a5a5a")

    selected_pdf_entry.bind("<Key>", lambda e: "break")

    choose_file_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/encryptpdf/choose_file_btn.png")
    choose_file_btn_label = Label(image=choose_file_btn_img)
    choose_file_btn_label.image = choose_file_btn_img
    choose_file_btn = Button(
        image = choose_file_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = get_pdf,
        relief = "flat")
    choose_file_btn.place(
        x = 333, y = 214,
        width = 314,
        height = 75)

    encrypt_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/encryptpdf/encrypt_btn.png")
    encrypt_btn_label = Label(image=encrypt_btn_img)
    encrypt_btn_label.image = encrypt_btn_img
    encrypt_btn = Button(
        image = encrypt_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = encrypt_pdf,
        relief = "flat")
    encrypt_btn.place(
        x = 1126, y = 658,
        width = 158,
        height = 49)

    encrypt_password_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/encryptpdf/encrypt_password_entry.png")
    encrypt_password_entry_bg = canvas.create_image(
        491.0, 422.5,
        image = encrypt_password_entry_img)
    encrypt_password_entry = Entry(
        bd = 0,
        font=("Poppins", 14),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#333333")
    encrypt_password_entry.place(
        x = 335, y = 404,
        width = 312,
        height = 35)

    

    