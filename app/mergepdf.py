from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showwarning, showerror, showinfo
from app.functionality import merge
from app import sidebar
from app.store import state, states
from app.utility import file_handler
import os

def load_merge_pdf(window):
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

    def btn_clicked():
        pass

    def get_pdf():
        if len(state.get_state(states.SELECTED_PDFS)) > 5:
            showwarning("Error" , "You can merge only 5 pdfs at a time")
            return
        pdf_path = filedialog.askopenfilename(initialdir=os.getenv("DEFAULT_SAVE_FOLDER"), title="Select a file" , filetypes=(("Pdf files","*.pdf*"),("all files","*.*")))
        filename = os.path.basename(pdf_path)
        if len(pdf_path) == 0:
            showwarning("Error" , "Please select a PDF file")
            return
        show_preview_pdf(filename, pdf_path)


    def merge_pdf():
        if len(state.get_state(states.SELECTED_PDFS)) < 2:
            showwarning("Error" , "Please select at least two PDF files")
            return
        try:
            result = merge.merge(state.get_state(states.SELECTED_PDFS))
            if result['status'] == 'success':
                file_handler.move_to_downloads('merged')
                showinfo('Success', result['message'])
            else:
                showwarning('Error', "An error has occurred")
        except Exception as e:
            print(e)
            showerror("Error" , "An error has occurred")

    def show_preview_pdf(filename, pdf_path):
        state.set_state(states.SELECTED_PDFS, state.get_state(states.SELECTED_PDFS) + [pdf_path])
        if len(state.get_state(states.SELECTED_PDFS)) == 1:
            selected_entry_1.insert(0, filename)
            selected_pdf_1_btn.place(
                x = 382, y = 430,
                width = 137,
                height = 159)
            selected_entry_1.place(
                x = 401, y = 556,
                width = 101,
                height = 13)
        if len(state.get_state(states.SELECTED_PDFS)) == 2:
            selected_entry_2.insert(0, filename)
            selected_pdf_2_btn.place(
                 x = 559, y = 430,
                width = 137,
                height = 159)
            selected_entry_2.place(
                x = 577, y = 556,
                width = 101,
                height = 13)
        if len(state.get_state(states.SELECTED_PDFS)) == 3:
            selected_entry_3.insert(0, filename)
            selected_pdf_3_btn.place(
                x = 736, y = 433,
                width = 137,
                height = 159)
            selected_entry_3.place(
                x = 753, y = 556,
                width = 101,
                height = 13)
        if len(state.get_state(states.SELECTED_PDFS)) == 4:
            selected_entry_4.insert(0, filename)
            selected_pdf_4_btn.place(
                x = 915, y = 430,
                width = 137,
                height = 159)
            selected_entry_4.place(
                x = 929, y = 556,
                width = 101,
                height = 13)
        if len(state.get_state(states.SELECTED_PDFS)) == 5:
            selected_entry_5.insert(0, filename)
            selected_pdf_5_btn.place(
                x = 1094, y = 430,
                width = 137,
                height = 159)
            selected_entry_5.place(
                x = 1113, y = 556,
                width = 101,
                height = 13)


    background_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = canvas.create_image(
        683.0, 384.0,
        image=background_img)


    selected_pdf_1 = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/selected_pdf_1.png")
    selected_pdf_btn_1_label = Label(image=selected_pdf_1)
    selected_pdf_btn_1_label.image = selected_pdf_1
    selected_pdf_1_btn = Button(
        image = selected_pdf_1,
        borderwidth = 0,
        highlightthickness = 0,
        background="#5a5a5a",
        activebackground="#5a5a5a",
        command = btn_clicked,
        relief = "flat")


    selected_pdf_2 = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/selected_pdf_2.png")
    selected_pdf_btn_2_label = Label(image=selected_pdf_2)
    selected_pdf_btn_2_label.image = selected_pdf_2
    selected_pdf_2_btn = Button(
        image = selected_pdf_2,
        borderwidth = 0,
        highlightthickness = 0,
        background="#5a5a5a",
        activebackground="#5a5a5a",
        command = btn_clicked,
        relief = "flat")


    selected_pdf_3 = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/selected_pdf_3.png")
    selected_pdf_btn_3_label = Label(image=selected_pdf_3)
    selected_pdf_btn_3_label.image = selected_pdf_3
    selected_pdf_3_btn = Button(
        image = selected_pdf_3,
        borderwidth = 0,
        highlightthickness = 0,
        background="#5a5a5a",
        activebackground="#5a5a5a",
        command = btn_clicked,
        relief = "flat")
        

    selected_pdf_4 = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/selected_pdf_4.png")
    selected_pdf_btn_4_label = Label(image=selected_pdf_4)
    selected_pdf_btn_4_label.image = selected_pdf_4
    selected_pdf_4_btn = Button(
        image = selected_pdf_4,
        borderwidth = 0,
        highlightthickness = 0,
        background="#5a5a5a",
        activebackground="#5a5a5a",
        command = btn_clicked,
        relief = "flat")


    selected_pdf_5 = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/selected_pdf_5.png")
    selected_pdf_btn_5_label = Label(image=selected_pdf_5)
    selected_pdf_btn_5_label.image = selected_pdf_5
    selected_pdf_5_btn = Button(
        image = selected_pdf_5,
        borderwidth = 0,
        highlightthickness = 0,
        background="#5a5a5a",
        activebackground="#5a5a5a",
        command = btn_clicked,
        relief = "flat")


    choose_file_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/choose_file_btn.png")
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


    merge_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/merge_btn.png")
    merge_btn_btn_label = Label(image=merge_btn_img)
    merge_btn_btn_label.image = merge_btn_img
    merge_btn = Button(
        image = merge_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = merge_pdf,
        relief = "flat")
    merge_btn.place(
        x = 1126, y = 658,
        width = 158,
        height = 49)


    selected_entry_1_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/selected_entry_1.png")
    selected_entry_1_bg = canvas.create_image(
        451.5, 563.5,
        image = selected_entry_1_img)
    selected_entry_1 = Entry(
        bd = 0,
        font=("Poppins", 8),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#5a5a5a")


    selected_entry_2_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/selected_entry_2.png")
    selected_entry_2_bg = canvas.create_image(
        627.5, 563.5,
        image = selected_entry_2_img)
    selected_entry_2 = Entry(
        bd = 0,
        font=("Poppins", 8),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#5a5a5a")


    selected_entry_3_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/selected_entry_3.png")
    selected_entry_3_bg = canvas.create_image(
        803.5, 563.5,
        image = selected_entry_3_img)
    selected_entry_3 = Entry(
        bd = 0,
        font=("Poppins", 8),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#5a5a5a")


    selected_entry_5_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/selected_entry_4.png")
    selected_entry_4_bg = canvas.create_image(
        979.5, 563.5,
        image = selected_entry_5_img)
    selected_entry_4 = Entry(
        bd = 0,
        font=("Poppins", 8),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#5a5a5a")


    selected_entry_5_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/mergepdf/selected_entry_5.png")
    selected_entry_5_bg = canvas.create_image(
        1163.5, 563.5,
        image = selected_entry_5_img)
    selected_entry_5 = Entry(
        bd = 0,
        font=("Poppins", 8),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#5a5a5a")


