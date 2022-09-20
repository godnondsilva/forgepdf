from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo, showwarning, showerror
from app.functionality import split, validate
from app import sidebar
from app.store import state, states
from app.utility import file_handler
import os

def load_split_pdf(window):
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


    def split_pdf():
        try:
            start_range = starting_range_entry.get()
            end_range = ending_range_entry.get()
                
            condition = validate.validate_split(start_range, end_range)
            if condition['status'] == 'error':
                showwarning('Error', condition['message'])
            else:
                start_range_integer = int(start_range)
                end_range_integer = int(end_range)

                #checking if we got exception in page ranges
                condition = split.spliter(start_range_integer, end_range_integer, state.get_state(states.SELECTED_PDF))
                if condition['status'] == 'error':
                    showwarning("Error" , "Please add the pages numbers within the range of the pdf.")
                else:
                    #Move the file to specific folder and move one copy to desktop
                    showinfo("Success" , "The pdf has been split successfully.")
                    file_handler.move_to_downloads('split')

        except Exception as e:
            showwarning("Error", e)
            
            
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

    
    background_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/splitpdf/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = canvas.create_image(
        683.0, 384.0,
        image=background_img)


    choose_file_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/splitpdf/choose_file_btn.png")
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


    split_pdf_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/splitpdf/split_pdf_btn.png")
    split_pdf_btn_label = Label(image=split_pdf_btn_img)
    split_pdf_btn_label.image = split_pdf_btn_img
    split_pdf_btn = Button(
        image = split_pdf_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = split_pdf,
        relief = "flat")
    split_pdf_btn.place(
        x = 1126, y = 658,
        width = 158,
        height = 49)


    selected_pdf_btn_image = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/splitpdf/selected_pdf_btn.png")
    selected_pdf_btn_label = Label(image=selected_pdf_btn_image)
    selected_pdf_btn_label.image = selected_pdf_btn_image
    selected_pdf_btn = Button(
        image = selected_pdf_btn_image,
        borderwidth = 0,
        highlightthickness = 0,
        background="#5a5a5a",
        activebackground="#5a5a5a",
        relief = "flat")


    selected_pdf_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/splitpdf/selected_pdf_entry.png")
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


    starting_range_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/splitpdf/starting_range_entry.png")
    starting_range_entry_bg = canvas.create_image(
        508.5, 423.5,
        image = starting_range_entry_img)
    starting_range_entry = Entry(
        bd = 0,
        font=("Poppins", 14),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#333333")
    starting_range_entry.place(
        x = 471, y = 405,
        width = 75,
        height = 35)


    ending_range_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/splitpdf/ending_range_entry.png")
    ending_range_entry_bg = canvas.create_image(
        508.5, 480.5,
        image = ending_range_entry_img)
    ending_range_entry = Entry(
        bd = 0,
        font=("Poppins", 14),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#333333")
    ending_range_entry.place(
        x = 471, y = 462,
        width = 75,
        height = 35)
