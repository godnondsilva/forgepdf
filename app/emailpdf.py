from tkinter import *
from tkinter import filedialog
from tkinter.font import families
from tkinter.messagebox import showerror, showwarning
from app import login
from app import home
from app.functionality import emailbot, emailvalidateapi
from app.user import user_details
from app.common import center
import os

class EmailPdfWindow():
    def __init__(self):
        #Window Config
        window = Tk()
        window.geometry("1280x720")
        window.configure(bg = "#0b132b")
        window.title('ForgePDF | Email PDF')
        center(window)

        #Variable to hold the attachment and csv address
        attachmentPath = []
        csvAddress = []
        haveAttachment = [False]


        #Button Functions
        def toHomePage():
            #reseting the setting of selected pdf
            user_details.NotSelectPdfBool()
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()

        
        def getAttachment():
            #gets attachement from user
            attachmentPathvar = filedialog.askopenfilename(initialdir= "D:\\Users\\ashis\\Desktop", title="Select a file" , filetypes=(("Pdf files","*.pdf*"),("all files","*.*")))
            filename = os.path.basename(attachmentPathvar)
            if len(attachmentPathvar) == 0:
                showwarning("Error" , "Please select a pdf file")
                return

            #stores attachement in list
            attachmentPath.append(attachmentPathvar)

            #adds the value in the textbox and displays it
            TextBoxAttachmentEntry.insert('0' , 'Attachment : ' + filename)
            TextBoxAttachmentEntry.bind("<Key>", lambda e: "break")
            haveAttachment[0] = True
            showAttachment()

        def ImportCSV():
            #gets csv from user
            csvAddressvar = filedialog.askopenfilename(initialdir= "D:\\Users\\ashis\\Desktop", title="Select a file" , filetypes=(("CSV files","*.csv*"),("all files","*.*")))
            filename = os.path.basename(csvAddressvar)
            if len(csvAddressvar) == 0:
                showwarning("Error" , "Please select a csv file")
                return

            #stores csv in list
            csvAddress.append(csvAddressvar)

            #adds the value in the textbox and displays it
            TextBoxCSVEntry.insert('0' , 'CSV File : ' + filename)
            TextBoxCSVEntry.bind("<Key>", lambda e: "break")
            showCSVFile()

        
        def SendEmail():
            # exception handling
            try:
                toaddress = EmailEntry.get()
                if len(csvAddress) == 0:
                    # check if the email is valid or not
                    condition = emailvalidateapi.getEmailValidate(toaddress)
                    if 'error' in condition:
                        showwarning("Error", condition['error'])
                        return
                #checks if the attachment is added or not
                if len(attachmentPath) == 0:
                    showwarning("Error" , "Please choose an attachment")
                    return

                #doesntsend email if there is ambiguity
                if toaddress != '' and len(csvAddress) != 0 :
                    showwarning("Error" , "Please choose any one way for email receipients.")
                    EmailEntry.insert('0' , '')
                    return

                #sends the email and shows that the email is sent
                showEmailSent()
                #giving priority on the csv emails then the ones typed
                if len(csvAddress) != 0 :
                    emailbot.csvToStr(csvAddress[0] , attachmentPath[0])
                else:
                    emailbot.emailbot(toaddress , attachmentPath[0])
            except:
                # show the error message
                showerror("Error" , "An error has occurred!")
                window.destroy()
                home.HomeWindow()
            
        #shows the the atttachment in the text box
        def showAttachment():
            AddAttachmentButton.destroy()
            TextBoxAttachmentEntry.pack()

            TextBoxAttachmentEntry.place(
            x = 50, y = 584,
            width = 536,
            height = 91)


            #if routed from options page then set the values for the pdf to be emailed
            if user_details.GetselectedPdfBool() == True:
                attachmentPath.append(user_details.getSelectPdf())
                TextBoxAttachmentEntry.insert('0' , 'Attachment : ' + os.path.basename(user_details.getSelectPdf()))
                TextBoxAttachmentEntry.bind("<Key>", lambda e: "break")


        #shows thw csv filr selected in a text box
        def showCSVFile():
            CSVFileButton.pack_forget()
            TextBoxCSVEntry.pack()

            TextBoxCSVEntry.place(
            x = 750, y = 377,
            width = 440,
            height = 63)

        #shows message that email is sent
        def showEmailSent():
            SendEmailButton.destroy()
            EmailSentLabel.pack()

            EmailSentLabel.place(
            x = 702, y = 584,
            width = 536,
            height = 91)


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


        #SendEmail Background image Config
        SendEmailBGImage = PhotoImage(file = f"./images/emailpdf/EmailPdfBG.png")
        SendEmailBG = canvas.create_image(
            640.0, 275.0,
            image=SendEmailBGImage)

       

        #Send email button config
        SendEmailImage = PhotoImage(file = f"./images/emailpdf/SendEmailBG.png")
        SendEmailButton = Button(
            image = SendEmailImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = SendEmail,
            relief = "flat")

        SendEmailButton.pack()

        SendEmailButton.place(
            x = 702, y = 584,
            width = 536,
            height = 91)


        #back button config
        BackImage = PhotoImage(file = f"./images/emailpdf/Back.png")
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


        #Import CSV file button config
        CSVFileImage = PhotoImage(file = f"./images/emailpdf/CSVFile.png")
        CSVFileButton = Button(
            image = CSVFileImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = ImportCSV,
            relief = "flat")

        CSVFileButton.pack()

        CSVFileButton.place(
            x = 750, y = 377,
            width = 440,
            height = 63)

        #Email Entry Config
        EmailEntryBGImage = PhotoImage(file = f"./images/emailpdf/EmailEntryBG.png")
        EmailEntryBG = canvas.create_image(
            315.0, 408.5,
            image = EmailEntryBGImage)

        EmailEntry = Entry(
            bd = 0,
            bg = "#1c2541",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#5BC0BE",
            highlightthickness = 0)

        EmailEntry.place(
            x = 95, y = 377,
            width = 440,
            height = 61)



        # Text Box for Attachment
        TextBoxAttachmentImage = PhotoImage(file = f"./images/emailpdf/TextboxBG.png")
        TextBoxAttachment = canvas.create_image(
            1124.5, 605.5,
            image = TextBoxAttachmentImage)

        TextBoxAttachmentEntry = Entry(
            bd = 0,
            bg = "#0B132B",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#0B132B",
            highlightthickness = 0)

        TextBoxAttachmentEntry.pack()
        TextBoxAttachmentEntry.pack_forget()

       


        #Text Box for CSV File
        TextBoxCSVImage = PhotoImage(file = f"./images/emailpdf/TextboxBG.png")
        TextBoxCSV = canvas.create_image(
            1124.5, 605.5,
            image = TextBoxCSVImage)

        TextBoxCSVEntry = Entry(
            bd = 0,
            bg = "#0B132B",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#0B132B",
            highlightthickness = 0)

        TextBoxCSVEntry.pack()
        TextBoxCSVEntry.pack_forget()

        #EmailSent Config
        EmailSentImage = PhotoImage(file = f"./images/emailpdf/Emailsent.png")
        EmailSent = canvas.create_image(
            1124.5, 605.5,
            image = TextBoxCSVImage)

        EmailSentLabel = Label(
            image = EmailSentImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            relief = "flat")

        EmailSentLabel.pack()
        EmailSentLabel.pack_forget()


        #Add Attachment config
        AddAttachmentImage = PhotoImage(file = f"./images/emailpdf/AddAttachmentBG.png")
        AddAttachmentButton = Button(
            image = AddAttachmentImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            command = getAttachment,
            relief = "flat")

        AddAttachmentButton.pack()

        
        if user_details.GetselectedPdfBool() == False and haveAttachment[0] == False:
            AddAttachmentButton.place(
                x = 50, y = 584,
                width = 536,
                height = 91)
        #if we have routed from options page then add the attachement from the pdf selected from options page
        else:
            showAttachment()
      

        #Additional window config
        window.resizable(False, False)
        window.iconbitmap('images/logo.ico')
        window.deiconify()
        window.mainloop()
