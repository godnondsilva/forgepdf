from tkinter import *
from tkinter.messagebox import showwarning, showerror
from tkinter import filedialog
from app import home
from app.common import center
import os, shutil
from app.functionality import extract, inputValidation
class extractWindow():
    def __init__(self):
        #Window Config
        window = Tk()
        window.geometry("1280x720")
        window.title('ForgePDF | Extract PDF')
        center(window)
        window.configure(bg = "#0b132b")
        
        # variable to store the pdf to extract
        self.pdfToExtract = ''

        #Button Functions
        def toHomePage():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()

        def getPDF():
            if self.pdfToExtract != '':
                showwarning("Error" , "You can extract only one pdf at a time")
                return
            attachmentPathvar = filedialog.askopenfilename(initialdir= "D:\\Users\\ashis\\Desktop", title="Select a file" , filetypes=(("Pdf files","*.pdf*"),("all files","*.*")))
            filename = os.path.basename(attachmentPathvar)
            if len(attachmentPathvar) == 0:
                showwarning("Error" , "Please select a pdf file")
                return
            PDFTextBoxEntry.insert('0' , filename)
            PDFTextBoxEntry.bind("<Key>", lambda e: "break")
            self.pdfToExtract = attachmentPathvar
            showExtractPDF()

        def extractPDF():
            try:
                condition = inputValidation.extractVal(self.pdfToExtract)
                if condition != True:
                    showwarning('Error', condition['error'])
                else:
                    isEmpty = extract.extract(self.pdfToExtract)
                    if isEmpty:
                        showerror('Error', 'Could not extract text from this pdf')
                        # if the extracted textfile is empty, go back to home frame
                        window.destroy()
                        home.HomeWindow()    
                    else:
                        MoveToDesktop()
                        showExtractedMessage()
            except:
                showerror("Error" , "An error has occurred!")
                window.destroy()
                home.HomeWindow()

        
        #Moves the files to desktop
        def MoveToDesktop():
            add = 'C:\\Users\\User\\Desktop\\ExtractedText.txt'
            shutil.move('output.txt' , add)


        #shows the selected pdf along with the name
        def showExtractPDF():
            PDFTextBoxEntry.pack()

            PDFTextBoxEntry.place(
            x = 1022, y = 385,
            width = 206,
            height = 28)

            PdfImageIcon.pack()

            PdfImageIcon.place(
            x = 1082, y = 273,
            width = 81,
            height = 87)


        #shows the message that pdf is extracted
        def showExtractedMessage():
            ExtractButton.pack_forget()
            PdfExtractedLabel.pack()

            PdfExtractedLabel.place(
            x = 1013, y = 602,
            width = 224,
            height = 48)


        #Creating a Canvas
        canvas = Canvas(
            window,
            bg = "#0b132b",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        #background Config
        ExtractPdfBGImage = PhotoImage(file = f"./images/extractpdf/extractpdfBG.png")
        ExtractPdfBG = canvas.create_image(
            640.0, 360.0,
            image=ExtractPdfBGImage)


        #Choose File Config
        ChooseFileImage = PhotoImage(file = f"./images/extractpdf/ChooseFile.png")
        ChooseFileButton = Button(
            image = ChooseFileImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = getPDF,
            relief = "flat")

        ChooseFileButton.place(
            x = 243, y = 344,
            width = 536,
            height = 100)

        #BackImage config
        BackImage = PhotoImage(file = f"./images/extractpdf/Back.png")
        BackButton = Button(
            image = BackImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = toHomePage,
            relief = "flat")

        BackButton.place(
            x = 17, y = 21,
            width = 139,
            height = 58)

        #ExtractButton config
        ExtractImage = PhotoImage(file = f"./images/extractpdf/Extract.png")
        ExtractButton = Button(
            image = ExtractImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = extractPDF,
            relief = "flat")

        ExtractButton.place(
            x = 1022, y = 604,
            width = 206,
            height = 46)

        #PdfTextBox
        PDFTextBoxImage = PhotoImage(file = f"./images/extractpdf/TextBoxBG.png")
        PDFTextBox = canvas.create_image(
            1125.0, 400.0,
            image = PDFTextBoxImage)

        PDFTextBoxEntry = Entry(
            bd = 0,
            bg = "#1C2541",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#1C2541",
            highlightthickness = 0)

        PDFTextBoxEntry.pack()
        PDFTextBoxEntry.pack_forget()

        #PDFExtracted Message
        PdfExtractedImage = PhotoImage(file = f"./images/extractpdf/Extracted.png")
        PdfExtractedLabel = Label(
            image = PdfExtractedImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            relief = "flat")

        PdfExtractedLabel.pack()
        PdfExtractedLabel.pack_forget()

        #PdfImage Config
        PdfImage = PhotoImage(file = f"./images/extractpdf/pdfImage.png")
        PdfImageIcon = Label(
            image = PdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            relief = "flat")

        PdfImageIcon.pack()
        PdfImageIcon.pack_forget()

        # additional config
        window.resizable(False, False)
        window.iconbitmap('images/logo.ico')
        window.deiconify()
        window.mainloop()
