from tkinter import *
from tkinter import filedialog
import mysql.connector
from app import home,emailpdf,mergepdf, splitpdf
from app import store
from app.utility import center
import os

class OptionsPdfWindow():
     def __init__(self):
        #Window Config
        window = Tk()
        window.geometry("1280x720")
        window.title('ForgePDF | PDF Options')
        window.configure(bg = "#0b132b")
        center(window)

        #Variable to hold the logged user user_id
        uid = [] 

        # Button functions
        def toHomePage():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()

        def toEmailPage():
            store.SetSelectedPdfBool()
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            emailpdf.EmailPdfWindow()

        def toSplitPdf():
            store.SetSelectedPdfBool()
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            splitpdf.SplitPdfWIndow()

        def toMergePdf():
            store.SetSelectedPdfBool()
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            mergepdf.MergePdfWindow()


        #Canvas Config
        canvas = Canvas(
            window,
            bg = "#0b132b",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)


        #Options page background config
        OptionPageBG = PhotoImage(file = f"./images/option/OptionsBG.png")
        OptionsPage = canvas.create_image(
            640.0, 360.0,
            image=OptionPageBG)


        #Back button
        BackButtonImage = PhotoImage(file = f"./images/option/Back.png")
        BackButton = Button(
            image = BackButtonImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = toHomePage,
            relief = "flat")

        BackButton.place(
            x = 27, y = 24,
            width = 139,
            height = 58)

        #Selected Pdf Label
        PdfSelectedImage = PhotoImage(file = f"./images/option/PdfSelected.png")
        PdfSelectLabel = Label(
            image = PdfSelectedImage,
            borderwidth = 0,
            background="#0B132B",
            activebackground="#0B132B",
            highlightthickness = 0,
            relief = "flat")

        PdfSelectLabel.place(
            x = 599, y = 246,
            width = 81,
            height = 87)

        #Email Pdf Button
        EmailPdfImage = PhotoImage(file = f"./images/option/EmailPdf.png")
        EmailPdfButton = Button(
            image = EmailPdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = toEmailPage,
            relief = "flat")

        EmailPdfButton.place(
            x = 0, y = 442,
            width = 391,
            height = 277)


        #SplitPdf Button
        SplitButtonBG = PhotoImage(file = f"./images/option/SplitPdf.png")
        SplitPdfButton = Button(
            image = SplitButtonBG,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = toSplitPdf,
            relief = "flat")

        SplitPdfButton.place(
            x = 397, y = 443,
            width = 510,
            height = 277)


        #MergePdf Button
        MergePdfBG = PhotoImage(file = f"./images/option/MergePdf.png")
        MergerPdfButton = Button(
            image = MergePdfBG,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = toMergePdf,
            relief = "flat")

        MergerPdfButton.place(
            x = 912, y = 443,
            width = 368,
            height = 277)


        #SelectPdf Name
        SelectedPdfImage = PhotoImage(file = f"./images/option/SelectPdfName.png")
        SelectedPdf = canvas.create_image(
            639.5, 369.0,
            image = SelectedPdfImage)

        SelectedPdfEntry = Entry(
            bd = 0,
            bg = "#0b132b",
            font = 20,
            fg= "#5BC0BE",
            justify= CENTER,
            insertbackground= "#0B132B",
            highlightthickness = 0)

        SelectedPdfEntry.insert('0',os.path.basename(store.getSelectPdf()))
        SelectedPdfEntry.bind("<Key>", lambda e: "break")

        SelectedPdfEntry.place(
            x = 323, y = 355,
            width = 633,
            height = 26)


        #Additional window config
        window.resizable(False, False)
        window.iconbitmap('images/logo.ico')
        window.deiconify()
        window.mainloop()

