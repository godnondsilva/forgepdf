from tkinter import *
from app import sidebar
from app.store import state, states
from app.utility import file_handler
import os

def load_home(window):
    
    def send_report():
        # Open mail application
        os.system("start mailto:godnondsilva@gmail.com")
    

    def send_feedback():
        os.system("start mailto:godnondsilva@gmail.com")
    

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
    

    background_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = canvas.create_image(
        671.0, 384.0,
        image=background_img)


    send_bug_report_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/send_bug_report_btn.png")
    send_bug_report_btn_label = Label(image=send_bug_report_btn_img)
    send_bug_report_btn_label.image = send_bug_report_btn_img
    send_bug_report_btn = Button(
        image = send_bug_report_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = send_report,
        relief = "flat")

    send_bug_report_btn.place(
        x = 358, y = 335,
        width = 114,
        height = 21)

    send_feedback_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/send_feedback_btn.png")
    send_feedback_btn_label = Label(image=send_feedback_btn_img)
    send_feedback_btn_label.image = send_feedback_btn_img
    send_feedback_btn = Button(
        image = send_feedback_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = send_feedback,
        relief = "flat")
    send_feedback_btn.place(
        x = 358, y = 358,
        width = 106,
        height = 21)


    view_more_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/view_more_btn.png")
    view_more_btn_label = Label(image=view_more_btn_img)
    view_more_btn_label.image = view_more_btn_img
    view_more_btn = Button(
        image = view_more_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = file_handler.open_folder,
        relief = "flat")
    view_more_btn.place(
        x = 522, y = 471,
        width = 145,
        height = 28)


    empty_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/empty.png")
    empty_label = Label(image = empty_img, bg = "#333333")
    empty_label.image = empty_img
    if len(state.get_state(states.PREVIEW_PDFS)) == 0:
        empty_label.place(
            x = 544, y = 590,
            width = 528,
            height = 50)
    else:
        if len(state.get_state(states.PREVIEW_PDFS)) >= 1:
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
            selected_pdf_btn.place(
                x = 382, y = 541,
                width = 137,
                height = 159)

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
            selected_pdf_entry.place(
                x = 399, y = 669,
                width = 101,
                height = 13)
            selected_pdf_entry.insert(0, state.get_state(states.PREVIEW_PDFS)[0])
            file_handler.open_file(state.get_state(states.PREVIEW_PDFS)[0])
        if len(state.get_state(states.PREVIEW_PDFS)) >= 2:
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
            selected_pdf_btn.place(
                x = 559, y = 541,
                width = 137,
                height = 159)

            selected_pdf_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/encryptpdf/selected_pdf_entry.png")
            selected_pdf_bg = canvas.create_image(
                1151.5, 381.5,
                image = selected_pdf_entry_img)
            selected_pdf_entry = Entry(
                bd = 0,
                text = state.get_state(states.PREVIEW_PDFS)[1],
                font=("Poppins", 8),
                highlightthickness = 0, 
                borderwidth=0,
                fg= "#FFFFFF",
                bg = "#5a5a5a")
            selected_pdf_entry.place(
                x = 576, y = 669,
                width = 101,
                height = 13)
            selected_pdf_entry.insert(0, state.get_state(states.PREVIEW_PDFS)[1])
            file_handler.open_file(state.get_state(states.PREVIEW_PDFS)[1])
        if len(state.get_state(states.PREVIEW_PDFS)) >= 3:
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
            selected_pdf_btn.place(
                x = 736, y = 541,
                width = 137,
                height = 159)
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
            selected_pdf_entry.place(
                x = 753, y = 669,
                width = 101,
                height = 13)
            selected_pdf_entry.insert(0, state.get_state(states.PREVIEW_PDFS)[2])
            file_handler.open_file(state.get_state(states.PREVIEW_PDFS)[2])
        if len(state.get_state(states.PREVIEW_PDFS)) >= 4:
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
            selected_pdf_btn.place(
                x = 913, y = 541,
                width = 137,
                height = 159)
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
            selected_pdf_entry.place(
                x = 930, y = 669,
                width = 101,
                height = 13)
            selected_pdf_entry.insert(0, state.get_state(states.PREVIEW_PDFS)[3])
            file_handler.open_file(state.get_state(states.PREVIEW_PDFS)[3])
        if len(state.get_state(states.PREVIEW_PDFS)) >= 5:
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
            selected_pdf_btn.place(
                x = 1090, y = 541,
                width = 137,
                height = 159)
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
            selected_pdf_entry.place(
                x = 1107, y = 669,
                width = 101,
                height = 13)
            selected_pdf_entry.insert(0, state.get_state(states.PREVIEW_PDFS)[4])
            file_handler.open_file(state.get_state(states.PREVIEW_PDFS)[4])