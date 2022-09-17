from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showwarning, showerror
from app import home, sidebar
from app.store import state, states
from app.functionality import decrypt, validate
import os, shutil
from pathlib import Path

def load_decrypt_pdf(window):
    #Canvas Config
    canvas = Canvas(
        window,
        bg = "#111111",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    sidebar.load_sidebar(window)

    def get_pdf():
        if state.get_state(states.SELECTED_PDF) != '':
            showwarning("Error" , "You can decrypt only one pdf at a time")
            return
        pdf_path = filedialog.askopenfilename(initialdir=os.getenv("DEFAULT_SAVE_FOLDER"), title="Select a file" , filetypes=(("Pdf files","*.pdf*"),("all files","*.*")))
        filename = os.path.basename(pdf_path)
        if len(pdf_path) == 0:
            showwarning("Error" , "Please select a PDF file")
            return
        show_preview_pdf(filename, pdf_path)

    def decrypt_pdf():
        password = decrypt_password_entry.get().strip()
        try:
            condition = validate.validate_decrypt(password)
            if condition != True:
                showwarning('Error', condition['error'])
            else:
                decrypt.decrypt(state.get_state(states.SELECTED_PDF), password)
                move_to_downloads()
                showwarning('Success', 'PDF decrypted successfully')
        except:
            showerror("Error" , "An error has occurred")
            home.HomeWindow()


    def move_to_downloads():
        path_to_download_folder = str(os.path.join(Path.home(), "Downloads/ForgePDF/"))
        new_name = 'forgepdf' + '1' + '.pdf'
        shutil.move('decrypted.pdf', path_to_download_folder+new_name)

        # store.IncrementCount()

        # add = 'C:\\Users\\User\\Downloads\\ForgePdf\\EncryptPdf' + str(store.getCount()+1) + '.pdf'
        
        #converts the address to form that can be saved in the database
        # newAdd = store.ConvertAddress(add)
        # saveToDB(newAdd)
    
    #Store the value in database
    # def saveToDB(add):
    #     execute_query("insert into files (file_address , user_id) values ('" + add + "',' " + str(store.getUID()) + "')")

    
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

    background_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/decryptpdf/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = canvas.create_image(
        805.5, 242.0,
        image=background_img)

    
    selected_pdf_btn_image = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/decryptpdf/selected_pdf_btn.png")
    selected_pdf_btn_label = Label(image=selected_pdf_btn_image)
    selected_pdf_btn_label.image = selected_pdf_btn_image
    selected_pdf_btn = Button(
        image = selected_pdf_btn_image,
        borderwidth = 0,
        highlightthickness = 0,
        background="#5a5a5a",
        activebackground="#5a5a5a",
        # command = get_pdf,
        relief = "flat")


    selected_pdf_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/decryptpdf/selected_pdf_entry.png")
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

    choose_file_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/decryptpdf/choose_file_btn.png")
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

    decrypt_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/decryptpdf/decrypt_btn.png")
    decrypt_btn_label = Label(image=decrypt_btn_img)
    decrypt_btn_label.image = decrypt_btn_img
    decrypt_btn = Button(
        image = decrypt_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = decrypt_pdf,
        relief = "flat")

    decrypt_btn.place(
        x = 1126, y = 658,
        width = 158,
        height = 49)

    decrypt_password_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/decryptpdf/decrypt_password_entry.png")
    decrypt_password_entry_bg = canvas.create_image(
        491.0, 422.5,
        image = decrypt_password_entry_img)

    decrypt_password_entry = Entry(
        bd = 0,
        font=("Poppins", 14),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#333333")

    decrypt_password_entry.place(
        x = 335, y = 404,
        width = 312,
        height = 35)
