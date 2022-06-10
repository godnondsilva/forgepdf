from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror
from tkinter.font import BOLD
from app import main, options, extractpdf, encryptpdf, emailpdf, mergepdf, savedpdfs, decryptpdf, splitpdf
from app.store import state
from app import store
from app.functionality import weather
import os
import mysql.connector
import datetime


def load_home(window):
    uid = []

    #Button Functions
    def toLoginPage():
        # destroy the current window instance (MainWindow)
        window.destroy()
        # call the auth window class which will load the login screen
        main.MainWindow()


    def toEncryptPDF():
            # destroy the current window instance (MainWindow)
        window.destroy()
        # call the encrypt pdf window class
        encryptpdf.encryptWindow()

    def toDecryptPDF():
            # destroy the current window instance (MainWindow)
        window.destroy()
        # call the decrypt pdf window class
        decryptpdf.decryptWindow()

    def toEmailPdf():
        # destroy the current window instance (MainWindow)
        window.destroy()
        # call the email pdf window class
        emailpdf.EmailPdfWindow()

    def toExtractPDF():
        # destroy the current window instance (MainWindow)
        window.destroy()
        # call the extract pdf window class
        extractpdf.extractWindow()


    def toSplitPdf():
            # destroy the current window instance (MainWindow)
        window.destroy()
        # call the splitPdf window class
        splitpdf.SplitPdfWIndow()
        
    def toMergedPdf():
        # destroy the current window instance (MainWindow)
        window.destroy()
        # call the merge pdf window class
        mergepdf.MergePdfWindow()

    def toSavedPdfs():
        # destroy the current window instance (MainWindow)
        window.destroy()
        # call the saved pdf window class
        savedpdfs.SavedPdfWindow()


    def toOptionsPage(SelectPdf):
        #set the value of the pdf select by the user in the user details class
        store.setSelectPdf(SelectPdf)

        # destroy the current window instance (MainWindow)
        window.destroy()
        # call the options up window class
        options.OptionsPdfWindow()
    

    # calling the weather api and storing the object in the variable weatherData
    weatherData=weather.get_weather()
    # if 'error' in weatherData:
    #     showerror('Error', weatherData['error'])
    #     window.destroy()
    print(weatherData)

    uid.append(store.getUID())
    
    # creating a mysql connection
    mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
    mycursor = mydb.cursor()
    # getting all the user data from the database
    mycursor.execute("select file_address from files where user_id='" + str(uid[0]) + "' order by file_id desc")
    # selecting only the first row from the fetched data
    result = mycursor.fetchall()
    print(result)


    canvas = Canvas(
        window,
        bg = "#0b132b",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./images/home/HomeBG.png")
    background = canvas.create_image(
        640.0, 360.0,
        image=background_img)

    # Image for Log Out
    logout_img = PhotoImage(file = f"./images/home/LogOut.png")
    logout_btn_label = Label(image=logout_img)
    logout_btn_label.image = logout_img
    # Log Out button config
    logout_btn = Button(
        canvas,
        image = logout_img,
        borderwidth = 0,
        highlightthickness = 0,
        activebackground= "#1C2541",
        command = toLoginPage,
        relief = "flat")

    # Logout button placement
    logout_btn.place(
        x = 22, y = 29,
        width = 131,
        height = 48)
        
    SplitPdfImage = PhotoImage(file = f"./images/home/SplitPdf.png")
    SplitPdfButton = Button(
        canvas,
        image = SplitPdfImage,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        command = toSplitPdf,
        relief = "flat")

    SplitPdfButton.place(
        x = 3, y = 573,
        width = 268,
        height = 144)

    MergePdfImage = PhotoImage(file = f"./images/home/MergePdf.png")
    MergePdfButton = Button(
        canvas,
        image = MergePdfImage,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        command = toMergedPdf,
        relief = "flat")

    MergePdfButton.place(
        x = 273, y = 573,
        width = 230,
        height = 144)

    SavedPdfImage = PhotoImage(file = f"./images/home/SavedPdf.png")
    SavedPdfButton = Button(
        canvas,
        image = SavedPdfImage,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        command = toSavedPdfs,
        relief = "flat")

    SavedPdfButton.place(
        x = 506, y = 573,
        width = 240,
        height = 144)

    ScrapyImage = PhotoImage(file = f"./images/home/Scrapy.png")
    ScrapyButton = Button(
        canvas,
        image = ScrapyImage,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        command = lambda: None,
        relief = "flat")

    ScrapyButton.place(
        x = 749, y = 573,
        width = 237,
        height = 144)

    EncryptPdfImage = PhotoImage(file = f"./images/home/EncryptPdf.png")
    EncryptPdfButton = Button(
        canvas,
        image = EncryptPdfImage,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        command = toEncryptPDF,
        relief = "flat")

    EncryptPdfButton.place(
        x = 274, y = 417,
        width = 229,
        height = 153)

    DecryptPdfImage = PhotoImage(file = f"./images/home/DecryptPdf.png")
    DecryptPdfButton = Button(
        canvas,
        image = DecryptPdfImage,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        command = toDecryptPDF,
        relief = "flat")

    DecryptPdfButton.place(
        x = 3, y = 417,
        width = 268,
        height = 153)

    EmailPdfImage = PhotoImage(file = f"./images/home/EmailPdf.png")
    EmailPdfButton = Button(
        canvas,
        image = EmailPdfImage,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        command = toEmailPdf,
        relief = "flat")

    EmailPdfButton.place(
        x = 506, y = 417,
        width = 240,
        height = 153)

    ExtractPdfImage = PhotoImage(file = f"./images/home/ExtractPdf.png")
    ExtractPdfButton = Button(
        canvas,
        image = ExtractPdfImage,
        borderwidth = 0,
        highlightthickness = 0,
        background="#1C2541",
        activebackground="#1C2541",
        command = toExtractPDF,
        relief = "flat")

    ExtractPdfButton.place(
        x = 748, y = 417,
        width = 237,
        height = 153)

    #-------------SQL QUERY------------------
    # creating a mysql connection
    mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
    mycursor = mydb.cursor()
    # getting all the user data from the database
    mycursor.execute("select file_address from files where user_id='" + str(state.get_uid()) + "' order by file_id desc")
    # selecting only the first row from the fetched data
    result = mycursor.fetchall()
    print(result)

    # creating a mysql connection
    mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
    mycursor = mydb.cursor()
    # getting all the user data from the database
    mycursor.execute("select count(*) from files")
    # selecting only the first row from the fetched data
    result1 = mycursor.fetchone()
    print(result1)
    store.SetCount(result1[0])
    
    
    Username = Label(text = store.getUsername(), font=('Poppins', 25, BOLD), fg= "#5BC0BE",bg = "#0B132B")
    Username.place(x = 280, y = 137)  

    SunnyImage = PhotoImage(file = f"./images/home/SunnyImage.png")
    CloudyImage = PhotoImage(file = f"./images/home/CloudyImage.png")
    RainyImage = PhotoImage(file = f"./images/home/RainyImage.png")
    WeatherImageButton = Label(
        bg="#0B132B",
        activebackground="#0B132B"
    )

    # setting the image for the button based on the description
    if weatherData['description'] == "clear sky":
        WeatherImageButton.config(image = SunnyImage)
    elif weatherData['description'] == "few clouds":
        WeatherImageButton.config(image = SunnyImage)
    elif weatherData['description'] == "scattered clouds":
        WeatherImageButton.config(image = SunnyImage)
    elif weatherData['description'] == "broken clouds":
        WeatherImageButton.config(image = CloudyImage)
    elif weatherData['description'] == "shower rain":
        WeatherImageButton.config(image = RainyImage)
    elif weatherData['description'] == "rain":
        WeatherImageButton.config(image = RainyImage)
    elif weatherData['description'] == "thunderstorm":
        WeatherImageButton.config(image = RainyImage)
    else:
        WeatherImageButton.config(image = CloudyImage)

    WeatherImageButton.place(
        x = 95, y = 252,
        width = 102,
        height = 94)

    WeatherDescTextBoxImage = PhotoImage(file = f"./images/home/WeatherDescTextBox.png")
    WeatherDescTextBox = canvas.create_image(
        143.5, 363.0,
        image = WeatherDescTextBoxImage)

    WeatherDescTextBoxEntry = Entry(
        bd = 0,
        bg = "#0b132b",
        font = ('Poppins', 16, BOLD),
        fg= "#5BC0BE",
        justify=CENTER,
        highlightthickness = 0)
    WeatherDescTextBoxEntry.insert(0, weatherData['description'].title())
    WeatherDescTextBoxEntry.bind("<Key>", lambda e: "break")

    WeatherDescTextBoxEntry.place(
        x = 63, y = 349,
        width = 161,
        height = 26)


    TempTextBoxImage = PhotoImage(file = f"./images/home/TempTextBox.png")
    TempTextBox = canvas.create_image(
        417.0, 349.5,
        image = TempTextBoxImage)

    TempTextBoxEntry = Entry(
        bd = 0,
        bg = "#0b132b",
        font = ('Poppins', 13, BOLD),
        fg= "#5BC0BE",
        justify=RIGHT,
        highlightthickness = 0)
    TempTextBoxEntry.insert(0, weatherData['temp'])
    TempTextBoxEntry.bind("<Key>", lambda e: "break")

    TempTextBoxEntry.place(
        x = 394, y = 339,
        width = 44,
        height = 23)



    FeelsLikeTextBoxImage = PhotoImage(file = f"./images/home/FeelsLikeTextBox.png")
    FeelsLikeTextBox = canvas.create_image(
        435.0, 381.5,
        image = FeelsLikeTextBoxImage)
    uid.append(store.getUID())
    

    FeelsLikeTextBoxEntry = Entry(
        bd = 0,
        bg = "#0b132b",
        font = ('Poppins', 13, BOLD),
        fg= "#5BC0BE",
        justify=RIGHT,
        highlightthickness = 0)
    FeelsLikeTextBoxEntry.insert(0, weatherData['feels_like'])
    FeelsLikeTextBoxEntry.bind("<Key>", lambda e: "break")

    FeelsLikeTextBoxEntry.place(
        x = 408, y = 370,
        width = 44,
        height = 23)



    WindTextBoxImage = PhotoImage(file = f"./images/home/WindTextBox.png")
    WindTextBox = canvas.create_image(
        626.0, 369.5,
        image = WindTextBoxImage)

    WindTextBoxEntry = Entry(
        bd = 0,
        bg = "#0b132b",
        font = ('Poppins', 15, BOLD),
        fg= "#5BC0BE",
        justify=CENTER,
        highlightthickness = 0)
    WindTextBoxEntry.insert(0, weatherData['wind_speed'])
    WindTextBoxEntry.bind("<Key>", lambda e: "break")

    WindTextBoxEntry.place(
        x = 597, y = 358,
        width = 53,
        height = 23)

    HumidityTextBoxImage = PhotoImage(file = f"./images/home/HumidityTextBox.png")
    HumidityTextBox = canvas.create_image(
        904.5, 369.5,
        image = HumidityTextBoxImage)

    HumidityTextBoxEntry = Entry(
        bd = 0,
        bg = "#0b132b",
        font = ('Poppins', 15, BOLD),
        fg= "#5BC0BE",
        justify=CENTER,
        highlightthickness = 0)
    HumidityTextBoxEntry.insert(0, weatherData['humidity'])
    HumidityTextBoxEntry.bind("<Key>", lambda e: "break")

    HumidityTextBoxEntry.place(
        x = 895, y = 358,
        width = 28,
        height = 23)

    DayTimeTextBoxImage = PhotoImage(file = f"./images/home/DayTimeTextBox.png")
    DayTimeTextBox = canvas.create_image(
        829.0, 159.5,
        image = DayTimeTextBoxImage)

    DayTimeTextBoxEntry = Entry(
        bd = 0,
        bg = "#0b132b",
        font = ('Poppins', 15, BOLD),
        fg= "#5BC0BE",
        justify=CENTER,
        highlightthickness = 0)
    DayTimeTextBoxEntry.insert(0, datetime.date.today().strftime("%A") + ', ' + datetime.datetime.now().strftime("%I:%M %p"))
    DayTimeTextBoxEntry.bind("<Key>", lambda e: "break")

    DayTimeTextBoxEntry.place(
        x = 706, y = 141,
        width = 246,
        height = 35)

    if len(result) > 0:
    # # Image for most recent Pdf in database
        Pdf1IconImage = PhotoImage(file = f"./images/home/Pdf1Icon.png")
    
        Pdf1IconLabel = Button(
            canvas,
            image = Pdf1IconImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = lambda: toOptionsPage(result[0][0]),
            relief = "flat")


        Pdf1IconLabel.place(
            x = 1057, y = 540,
            width = 156,
            height = 126)

        
        #PDF1 name box
        Pdf1TextBoxImage = PhotoImage(file = f"./images/home/TextBox1.png")
        Pdf1TextBox = canvas.create_image(
            1135.0, 648.0,
            image = Pdf1TextBoxImage)

        Pdf1Entry = Entry(
            bd = 0,
            bg = "#1c2541",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#1C2541",
            highlightthickness = 0)

        Pdf1Entry.place(
            x = 1057, y = 633,
            width = 156,
            height = 28)

        Pdf1Entry.insert('0' , os.path.basename(result[0][0]))
        Pdf1Entry.bind("<Key>", lambda e: "break")

    
    if len(result) > 1:
    # # Image for 2nd most recent Pdf in database
        Pdf2IconImage = PhotoImage(file = f"./images/home/Pdf2Icon.png")
        
        Pdf2IconLabel = Button(
            canvas,
            image = Pdf2IconImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command = lambda: toOptionsPage(result[1][0]),
            relief = "flat")

        Pdf2IconLabel.place(
            x = 1057, y = 374,
            width = 156,
            height = 126)

        #PDF2 name box
        Pdf2TextBoxImage = PhotoImage(file = f"./images/home/TextBox2.png")
        Pdf2TextBox = canvas.create_image(
            1135.0, 648.0,
            image = Pdf2TextBoxImage)

        Pdf2Entry = Entry(
            bd = 0,
            bg = "#1c2541",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#1C2541",
            highlightthickness = 0)

        Pdf2Entry.place(
            x = 1057, y = 467,
            width = 156,
            height = 28)

        Pdf2Entry.insert('0' , os.path.basename(result[1][0]))
        Pdf2Entry.bind("<Key>", lambda e: "break")

    if len(result) > 2:
    # # Image for 3rd most recent Pdf in database
        Pdf3IconImage = PhotoImage(file = f"./images/home/Pdf3Icon.png")
        
        Pdf3IconLabel = Button(
            canvas,
            image = Pdf3IconImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#1C2541",
            activebackground="#1C2541",
            command =lambda: toOptionsPage(result[2][0]),
            relief = "flat")


        Pdf3IconLabel.place(
            x = 1057, y = 208,
            width = 156,
            height = 126)

        #PDF3 name box
        Pdf3TextBoxImage = PhotoImage(file = f"./images/home/TextBox3.png")
        Pdf2TextBox = canvas.create_image(
            1135.0, 648.0,
            image = Pdf3TextBoxImage)

        Pdf3Entry = Entry(
            bd = 0,
            bg = "#1c2541",
            font = 20,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#1C2541",
            highlightthickness = 0)

        Pdf3Entry.place(
            x = 1057, y = 301,
            width = 156,
            height = 28)

        Pdf3Entry.insert('0' , os.path.basename(result[2][0]))
        Pdf3Entry.bind("<Key>", lambda e: "break")



    if len(result) == 0:
        # Image for 3rd most recent Pdf in database
        NotFoundImage = PhotoImage(file = f"./images/home/notFound.png")
        
        NotFoundLabel = Label(
            image = NotFoundImage,
            background="#1C2541",
            activebackground="#1C2541"
        )


        NotFoundLabel.place(
            x = 1042, y = 250,
            width = 176,
            height = 231)

    