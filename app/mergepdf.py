from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showwarning, showerror

import PyPDF2
from app.functionality import merge
from app import store
from app import login
from app import home
from app.utility import center,execute_query
import os
import shutil

def load_merge_pdf(window):
    #Variable to store the pdfs selected so far
    pdfstomerge = []

    #selects the pdf for merging
    def selectPdf():
        canget = True #allows the user to chose the file if already 3 files are not selected

        #shows error if the user tries to choose a pdf file after 3 files have already been choosed
        if Pdf1name.get() != '' and Pdf2name.get() != '' and Pdf3name.get() != '':
            showwarning("Error" , "You cannot add more than 3 pdfs to merge, sorry for the inconvenience!")
            canget = False

        #opens the file box , gets the abs path of the file and appends in list
        if canget == True:    
            fileaddress = filedialog.askopenfilename(initialdir= os.getenv('MERGE_INITIAL_DIR'), title="Select a file" , filetypes=(("Pdf files","*.pdf*"),("all files","*.*")))
            print(fileaddress)
            if len(fileaddress) == 0:
                showwarning("Error" , "Please select a pdf file")
                return
            pdfstomerge.append(fileaddress)
            filename = os.path.basename(fileaddress)
            print(filename)

        
        #fills the first space if the input is empty
        if Pdf1name.get() == '':
            Pdf1name.insert('0',filename)
            Pdf1name.bind("<Key>", lambda e: "break")
            showPdf1pic()

        #fills the second space if the input is empty
        elif Pdf2name.get() == '':
            Pdf2name.insert('0',filename)
            Pdf2name.bind("<Key>", lambda e: "break")
            showPdf2pic()

        #fills the third space if the input is empty
        elif Pdf3name.get() == '':
            Pdf3name.insert('0',filename)
            Pdf3name.bind("<Key>", lambda e: "break")
            showPdf3pic()
        
    #shows the first pdf pic
    def showPdf1pic():
        Pdf1Label.pack()
        Pdf1Label.place(
        x = 1082, y = 495,
        width = 81,
        height = 87)

        #if routed from options page then set the values of the pdf to be merged
        if store.GetselectedPdfBool() == True:
            pdfstomerge.append(store.getSelectPdf())
            Pdf1name.insert('0', os.path.basename(store.getSelectPdf()))
            Pdf1name.bind("<Key>", lambda e: "break")


    #shows the second pdf pic
    def showPdf2pic():
        Pdf2Label.pack()
        Pdf2Label.place(
        x = 1079, y = 344,
        width = 81,
        height = 87)

    #shows the third pdf pic
    def showPdf3pic():
        Pdf3Label.pack()
        Pdf3Label.place(
        x = 1079, y = 190,
        width = 81,
        height = 87)


    #merges the files , shows the merge message and hides the button
    def mergePdf():
        try:
            print(pdfstomerge)
            merge.merge(pdfstomerge) #call the merge function to merge
            MergeButton.pack_forget()
            FilesMergedLabel.pack()

            FilesMergedLabel.place(
            x = 1024, y = 651,
            width = 204,
            height = 46)

            #Move the file to specific folder and move one copy to desktop
            MoveToFolder()
        except:
            showerror("Error" , "An error has occurred")
            window.destroy()
            home.HomeWindow()

    #Moves the files to a specific directory and copies to desktop
    def MoveToFolder():

        #increment the count of the pdf to prevent overwriting
        store.IncrementCount()
        add = 'C:\\Users\\User\\Downloads\\ForgePdf\\MergePdf' + str(store.getCount()+1) + '.pdf'
        shutil.move('Merge.pdf' , add)
        shutil.copy(add , 'C:\\Users\\User\\Desktop')
        
        #converts the address to form that can be saved in the database
        newAdd = store.ConvertAddress(add)
        saveToDB(newAdd)
    
    #Store the value in database
    def saveToDB(add):
        execute_query("insert into files (file_address , user_id) values ('" + add + "',' " + str(store.getUID()) + "')")

#----------------------------------------------------
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


    #MergePdfBG
    MergePdfBGImage = PhotoImage(file = f"./images/mergepdf/MergePdfBG.png")
    MergePdfBG = canvas.create_image(
        640.5, 360.0,
        image=MergePdfBGImage)

    #ChooseFile Button Config 
    ChooseFileBGImage = PhotoImage(file = f"./images/mergepdf/ChooseFile.png")
    ChooseFileButton = Button(
        image = ChooseFileBGImage,
        borderwidth = 0,
        highlightthickness = 0,
        background="#0B132B",
        activebackground="#0B132B",
        command = selectPdf,
        relief = "flat")

    ChooseFileButton.place(
        x = 243, y = 344,
        width = 536,
        height = 100)


    
    #Back Button Config
    BackBGImage = PhotoImage(file = f"./images/mergepdf/Back.png")
    BackButton = Button(
        image = BackBGImage,
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


    #Merge Button Config
    MergeBGImage = PhotoImage(file = f"./images/mergepdf/MergerButton.png")
    MergeButton = Button(
        image = MergeBGImage,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        command = mergePdf,
        relief = "flat")

    MergeButton.pack()

    MergeButton.place(
        x = 1024, y = 651,
        width = 204,
        height = 46)

    


    #Pdf1 Config
    Pdf1Image = PhotoImage(file = f"./images/mergepdf/pdf1.png")
    Pdf1Label = Label(
        image = Pdf1Image,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        relief = "flat")

    Pdf1Label.place(
        x = 1082, y = 495,
        width = 81,
        height = 87)

    #Hiding the pdf and showing only when a pdf is selected
    Pdf1Label.pack()
    Pdf1Label.pack_forget()


    #Pdf2 Config
    Pdf2Image = PhotoImage(file = f"./images/mergepdf/pdf2.png")
    Pdf2Label = Label(
        image = Pdf2Image,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        relief = "flat")

    Pdf2Label.place(
        x = 1079, y = 344,
        width = 81,
        height = 87)

    #Hiding the pdf and showing only when a pdf is selected
    Pdf2Label.pack()
    Pdf2Label.pack_forget()


    #Pdf3 Config
    Pdf3Image = PhotoImage(file = f"./images/mergepdf/pdf3.png")
    Pdf3Label = Label(
        image = Pdf3Image,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        relief = "flat")

    Pdf3Label.place(
        x = 1079, y = 190,
        width = 81,
        height = 87)

    #Hiding the pdf and showing only when a pdf is selected
    Pdf3Label.pack()
    Pdf3Label.pack_forget()


    #Pdf1 file name Config
    Pdf1nameImage = PhotoImage(file = f"./images/mergepdf/pdf1name.png")
    Pdf1name = canvas.create_image(
        1124.5, 605.5,
        image = Pdf1nameImage)

    Pdf1name = Entry(
        bd = 0,
        bg = "#1c2541",
        font = 20,
        fg= "#5BC0BE",
        justify=CENTER,
        insertbackground= "#1C2541",
        highlightthickness = 0)

    Pdf1name.place(
        x = 1008, y = 592,
        width = 233,
        height = 25)


    #Pdf2 file name Config
    Pdf2nameImage = PhotoImage(file = f"./images/mergepdf/pdf2name.png")
    Pdf2name = canvas.create_image(
        1126.0, 453.0,
        image = Pdf2nameImage)

    Pdf2name = Entry(
        bd = 0,
        bg = "#1c2541",
        font = 20,
        fg= "#5BC0BE",
        justify=CENTER,
        insertbackground= "#1C2541",
        highlightthickness = 0)

    Pdf2name.place(
        x = 1011, y = 439,
        width = 230,
        height = 26)


    #Pdf3 file name Config
    Pdf3nameImage = PhotoImage(file = f"./images/mergepdf/pdf3name.png")
    Pdf3name = canvas.create_image(
        1125.5, 300.5,
        image = Pdf3nameImage)

    Pdf3name = Entry(
        bd = 0,
        bg = "#1c2541",
        font = 20,
        fg= "#5BC0BE",
        justify=CENTER,
        insertbackground= "#1C2541",
        highlightthickness = 0)

    Pdf3name.place(
        x = 1019, y = 282,
        width = 213,
        height = 35)

    #Pdf merges dialouge
    FilesMergedImage = PhotoImage(file = f"./images/mergepdf/FilesMerged.png")
    FilesMergedLabel = Label(
        image = FilesMergedImage,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        relief = "flat")

    FilesMergedLabel.place(
        x = 1024, y = 651,
        width = 204,
        height = 46)

    FilesMergedLabel.pack()
    FilesMergedLabel.pack_forget()


    #if we are routing from options page then set the pdf was the select in options page
    # if store.GetselectedPdfBool() == True:
    #     showPdf1pic()


