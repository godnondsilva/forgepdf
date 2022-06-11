from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showwarning, showerror
from app import home
from app.store import state
from app.functionality import decrypt, validate
from app.utility import center, executeQuery
import os, shutil

class decryptWindow():
    def __init__(self):
        #Window Config
        window = Tk()
        window.geometry("1280x720")
        window.title('ForgePDF | Decrypt PDF')
        center(window)
        window.configure(bg = "#0b132b")
        
        # variable to store the pdf to decrypt
        self.pdfToDecrypt = ''

        #Button Functions
        def toHomePage():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()

        #gets the pdf to decrypt
        def getPdf():
            if self.pdfToDecrypt != '':
                showwarning("Error" , "You can decrypt only one pdf at a time")
                return
            #gets attachement from user
            attachmentPathvar = filedialog.askopenfilename(initialdir= "D:\\Users\\ashis\\Desktop", title="Select a file" , filetypes=(("Pdf files","*.pdf*"),("all files","*.*")))
            filename = os.path.basename(attachmentPathvar)
            if len(attachmentPathvar) == 0:
                showwarning("Error" , "Please select a pdf file")
                return
            #adds the value in the textbox and displays it
            PDFTextBoxEntry.insert('0' , filename)
            PDFTextBoxEntry.bind("<Key>", lambda e: "break")
            self.pdfToDecrypt = attachmentPathvar
            showDecryptPdf()


        # function to decrypt the pdf
        def DecryptPdf():
            # getting the password 
            password = PasswordEntry.get()
            # stripping the password and storing it in a variable
            new_password = password.strip()
            # exception handling 
            try:
                condition = validate.validate_decrypt(new_password)
                if condition != True:
                    showwarning('Error', condition['error'])
                else:
                    condition,message = decrypt.decrypt(self.pdfToDecrypt, new_password)
                    if condition == False:
                        showwarning("Error", message)
                        if message == 'This pdf is NOT Encrypted!':
                            window.destroy()
                            home.HomeWindow()
                        return 
                    showPdfDecryptMessage()
                    MoveToFolder()
            except Exception as e:
                print(e)
                showerror("Error" , "An error has occurred!")
                window.destroy()
                home.HomeWindow()

        #Moves the files to a specific directory and copies to desktop
        def MoveToFolder():
            #increment the count of the pdf to prevent overwriting
            state.IncrementCount()
            add = 'C:\\Users\\User\\Downloads\\ForgePdf\\DecryptPdf' + str(state.getCount()+1) + '.pdf'
            shutil.move('decrypted.pdf' , add)
            shutil.copy(add , 'C:\\Users\\User\\Desktop')
            
            #converts the address to form that can be saved in the database
            newAdd = state.ConvertAddress(add)
            saveToDB(newAdd)
        
        #Store the value in database
        def saveToDB(add):
            executeQuery("insert into files (file_address , user_id) values ('" + add + "',' " + str(state.getUID()) + "')")

       
        #shows the selected pdf along with the name
        def showDecryptPdf():
            PDFTextBoxEntry.pack()

            PDFTextBoxEntry.place(
            x = 100, y = 600,
            width = 800,
            height = 87)

            PdfImageIcon.pack()

            PdfImageIcon.place(
            x = 100, y = 525,
            width = 800,
            height = 87)


        #shows the message that pdf is encypted
        def showPdfDecryptMessage():
            DecryptPdfSubmitButton.pack_forget()
            PdfDecryptLabel.pack()

            PdfDecryptLabel.place(
            x = 1012, y = 604,
            width = 230,
            height = 46)


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


        #DecryptPdf  background Config
        decryptpdfBGImage = PhotoImage(file =  f"./images/decryptpdf/decryptpdfBG.png")
        decryptpdfBG = canvas.create_image(
            640.0, 360.0,
            image=decryptpdfBGImage)


        #ChooseFile BG
        ChooseFileImage = PhotoImage(file = f"./images/decryptpdf/ChooseFile.png")
        ChooseFileButton = Button(
            image = ChooseFileImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = getPdf,
            relief = "flat")

        ChooseFileButton.place(
            x = 243, y = 344,
            width = 536,
            height = 100)


        #BackButton Config
        BackButtonImage = PhotoImage(file = f"./images/decryptpdf/BackButton.png")
        BackButton = Button(
            image = BackButtonImage,
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


        #Decrypt pdf button config
        DecryptPdfImage = PhotoImage(file = f"./images/decryptpdf/Decrypt.png")
        DecryptPdfSubmitButton = Button(
            image = DecryptPdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = DecryptPdf,
            relief = "flat")

        DecryptPdfSubmitButton.place(
            x = 1022, y = 604,
            width = 206,
            height = 46)


        #Ending Range Entry Config
        passwordEntryImage = PhotoImage(file = f"./images/decryptpdf/TextBox.png")
        PasswordEntryCanvasImage = canvas.create_image(
            1124.0, 443.0,
            image = passwordEntryImage)

        PasswordEntry = Entry(
            bd = 0,
            bg = "#0b132b",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#5BC0BE",
            highlightthickness = 0)

        PasswordEntry.place(
            x = 987, y = 410,
            width = 274,
            height = 66)

        
        #PdfTextBox
        PDFTextBoxImage = PhotoImage(file = f"./images/decryptpdf/TextboxBG.png")
        PDFTextBox = canvas.create_image(
            1124.5, 605.5,
            image = PDFTextBoxImage)

        PDFTextBoxEntry = Entry(
            bd = 0,
            bg = "#0B132B",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#0B132B",
            highlightthickness = 0)

        PDFTextBoxEntry.pack()
        PDFTextBoxEntry.pack_forget()


        #PdfMerged Message
        PdfDecryptImage = PhotoImage(file = f"./images/decryptpdf/Decrypted.png")
        PdfDecryptLabel = Label(
            image = PdfDecryptImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            relief = "flat")

        PdfDecryptLabel.pack()
        PdfDecryptLabel.pack_forget()


        #PdfImage Config
        PdfImage = PhotoImage(file = f"./images/decryptpdf/pdfImage.png")
        PdfImageIcon = Label(
            image = PdfImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            relief = "flat")

        PdfImageIcon.pack()
        PdfImageIcon.pack_forget()

        # additional window config
        window.resizable(False, False)
        window.iconbitmap('images/logo.ico')
        window.deiconify()
        window.mainloop()
