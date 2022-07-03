from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror
from tkinter.font import BOLD
from app import main, options, extractpdf, encryptpdf, emailpdf, mergepdf, savedpdfs, decryptpdf, splitpdf
from app.store import state, states
from app import store
from app.functionality import weather, thought
from app.utility import get_cursor_data
import datetime


def load_home(window):
    #Button Functions
    def route_login():
        # call the auth window class which will load the login screen
        main.MainWindow()


    def route_encypt_pdf():
        # call the encrypt pdf window class
        encryptpdf.encryptWindow()

    def route_decrypt_pdf():
        # call the decrypt pdf window class
        decryptpdf.decryptWindow()

    def route_email_pdf():
        # call the email pdf window class
        emailpdf.EmailPdfWindow()

    def route_extract_pdf():
        # call the extract pdf window class
        extractpdf.extractWindow()


    def route_split_pdf():
        # call the splitPdf window class
        splitpdf.SplitPdfWIndow()
        
    def route_merge_pdf():
        # call the merge pdf window class
        mergepdf.MergePdfWindow()

    def route_saved_pdf():
        # call the saved pdf window class
        savedpdfs.SavedPdfWindow()


    def route_options(SelectPdf):
        #set the value of the pdf select by the user in the user details class
        store.setSelectPdf(SelectPdf)
        # call the options up window class
        options.OptionsPdfWindow()
    
    def btn_clicked():
        pass
    
    canvas = Canvas(
        window,
        bg = "#111111",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./images/home/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = canvas.create_image(
        671.0, 384.0,
        image=background_img)

    logout_btn_img = PhotoImage(file = f"./images/home/logout_btn.png")
    logout_btn_label = Label(image=logout_btn_img)
    logout_btn_label.image = logout_btn_img
    logout_btn = Button(
        image = logout_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        # command = btn_clicked,
        relief = "flat")

    logout_btn.place(
        x = 1122, y = 35,
        width = 160,
        height = 45)

    encrypt_btn_img = PhotoImage(file = f"./images/home/encrypt_btn.png")
    encrypt_btn_label = Label(image=encrypt_btn_img)
    encrypt_btn_label.image = encrypt_btn_img
    encrypt_btn = Button(
        image = encrypt_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    encrypt_btn.place(
        x = 38, y = 188,
        width = 105,
        height = 27)

    decrypt_btn_img = PhotoImage(file = f"./images/home/decrypt_btn.png")
    decrypt_btn_label = Label(image=decrypt_btn_img)
    decrypt_btn_label.image = decrypt_btn_img
    decrypt_btn = Button(
        image = decrypt_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    decrypt_btn.place(
        x = 38, y = 222,
        width = 108,
        height = 27)

    email_btn_img = PhotoImage(file = f"./images/home/email_btn.png")
    email_btn_label = Label(image=email_btn_img)
    email_btn_label.image = email_btn_img
    email_btn = Button(
        image = email_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    email_btn.place(
        x = 38, y = 256,
        width = 86,
        height = 27)

    extract_btn_img = PhotoImage(file = f"./images/home/extract_btn.png")
    extract_btn_label = Label(image=extract_btn_img)
    extract_btn_label.image = extract_btn_img
    extract_btn = Button(
        image = extract_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    extract_btn.place(
        x = 38, y = 290,
        width = 98,
        height = 27)

    split_btn_img = PhotoImage(file = f"./images/home/split_btn.png")
    split_btn_label = Label(image=split_btn_img)
    split_btn_label.image = split_btn_img
    split_btn = Button(
        image = split_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    split_btn.place(
        x = 38, y = 324,
        width = 76,
        height = 27)

    merge_btn_img = PhotoImage(file = f"./images/home/merge_btn.png")
    merge_btn_label = Label(image=merge_btn_img)
    merge_btn_label.image = merge_btn_img
    merge_btn = Button(
        image = merge_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    merge_btn.place(
        x = 38, y = 358,
        width = 94,
        height = 27)

    send_bug_report_btn_img = PhotoImage(file = f"./images/home/send_bug_report_btn.png")
    send_bug_report_btn_label = Label(image=send_bug_report_btn_img)
    send_bug_report_btn_label.image = send_bug_report_btn_img
    send_bug_report_btn = Button(
        image = send_bug_report_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    send_bug_report_btn.place(
        x = 358, y = 378,
        width = 114,
        height = 21)

    send_feedback_btn_img = PhotoImage(file = f"./images/home/send_feedback_btn.png")
    send_feedback_btn_label = Label(image=send_feedback_btn_img)
    send_feedback_btn_label.image = send_feedback_btn_img
    send_feedback_btn = Button(
        image = send_feedback_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#333333",
        activebackground="#333333",
        command = btn_clicked,
        relief = "flat")

    send_feedback_btn.place(
        x = 358, y = 356,
        width = 106,
        height = 21)

    view_more_btn_img = PhotoImage(file = f"./images/home/view_more_btn.png")
    view_more_btn_label = Label(image=view_more_btn_img)
    view_more_btn_label.image = view_more_btn_img
    view_more_btn = Button(
        image = view_more_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = btn_clicked,
        relief = "flat")

    view_more_btn.place(
        x = 522, y = 471,
        width = 145,
        height = 28)
    
    thought_text = Text(window, 
        height=549, 
        width=259, 
        wrap=WORD,
        font=("Poppins", 11),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#CCCCCC",
        bg = "#333333")

    thought_text.place(
        x = 358, y = 221,
        width = 358,
        height = 74)

    name_text = Text(window, 
        height=549, 
        width=259, 
        wrap=WORD,
        font=("Poppins", 18),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#333333")

    name_text.place(
        x = 358, y = 135,
        width = 250,
        height = 36)

    datetime_entry_img = PhotoImage(file = f"./images/home/datetime_entry.png")
    datetime_entry_bg = canvas.create_image(
        927.5, 156.5,
        image = datetime_entry_img)

    datetime_entry = Entry(
        bd = 0,
        font=("Poppins", 10),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#2F8FFF",
        bg = "#333333")

    datetime_entry.place(
        x = 860, y = 146,
        width = 115,
        height = 19)

    location_entry_img = PhotoImage(file = f"./images/home/location_entry.png")
    location_entry_bg = canvas.create_image(
        955.0, 179.0,
        image = location_entry_img)

    location_entry = Entry(
        bd = 0,
        font=("Poppins", 14),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#333333")

    location_entry.place(
        x = 860, y = 167,
        width = 170,
        height = 22)

    # Configuration
    thought_text_value = thought.get_thought()
    thought_text.insert(END, thought_text_value)
    thought_text.config(state=DISABLED)

    name_text_value = state.get_state(states.USERNAME)
    if 'error' in name_text_value:
        showerror('Error', name_text_value['error'])
    name_text.insert(END, "Welcome, "+name_text_value.title())
    name_text.config(state=DISABLED)

    # calling the weather api and storing the object in the variable weatherData
    weatherData = weather.get_weather(state.get_state(states.LOCATION))
    if 'error' in weatherData:
        showerror('Error', weatherData['error'])
    print(weatherData)

    datetime_entry.insert(0, datetime.date.today().strftime("%A") + ', ' + datetime.datetime.now().strftime("%I:%M %p"))
    datetime_entry.bind("<Key>", lambda e: "break")

    location_entry.insert(0, "Mangalore")
    location_entry.bind("<Key>", lambda e: "break")

    # # creating a mysql connection
    # mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
    # mycursor = mydb.cursor()
    # # getting all the user data from the database
    # mycursor.execute("select file_address from files where user_id='" + str(uid[0]) + "' order by file_id desc")
    # # selecting only the first row from the fetched data
    # result = mycursor.fetchall()
    # print(result)

    # result = get_cursor_data("select file_address from files where user_id='" + str(store.getUID()) + "' order by file_id desc")

#####################################################################

    # #-------------SQL QUERY------------------
    # # creating a mysql connection
    # mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
    # mycursor = mydb.cursor()
    # # getting all the user data from the database
    # mycursor.execute("select file_address from files where user_id='" + str(state.get_state(states.UID)) + "' order by file_id desc")
    # # selecting only the first row from the fetched data
    # result = mycursor.fetchall()
    # print(result)

    # # creating a mysql connection
    # mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
    # mycursor = mydb.cursor()
    # # getting all the user data from the database
    # mycursor.execute("select count(*) from files")
    # # selecting only the first row from the fetched data
    # result1 = mycursor.fetchone()
    # print(result1)
    # store.SetCount(result1[0])
    

#####################################################################

    # SunnyImage = PhotoImage(file = f"./images/home/SunnyImage.png")
    # CloudyImage = PhotoImage(file = f"./images/home/CloudyImage.png")
    # RainyImage = PhotoImage(file = f"./images/home/RainyImage.png")
    # WeatherImageButton = Label(
    #     bg="#0B132B",
    #     activebackground="#0B132B"
    # )

    # # setting the image for the button based on the description
    # if weatherData['description'] == "clear sky":
    #     WeatherImageButton.config(image = SunnyImage)
    # elif weatherData['description'] == "few clouds":
    #     WeatherImageButton.config(image = SunnyImage)
    # elif weatherData['description'] == "scattered clouds":
    #     WeatherImageButton.config(image = SunnyImage)
    # elif weatherData['description'] == "broken clouds":
    #     WeatherImageButton.config(image = CloudyImage)
    # elif weatherData['description'] == "shower rain":
    #     WeatherImageButton.config(image = RainyImage)
    # elif weatherData['description'] == "rain":
    #     WeatherImageButton.config(image = RainyImage)
    # elif weatherData['description'] == "thunderstorm":
    #     WeatherImageButton.config(image = RainyImage)
    # else:
    #     WeatherImageButton.config(image = CloudyImage)

    # WeatherImageButton.place(
    #     x = 95, y = 252,
    #     width = 102,
    #     height = 94)

    # WeatherDescTextBoxImage = PhotoImage(file = f"./images/home/WeatherDescTextBox.png")
    # WeatherDescTextBox = canvas.create_image(
    #     143.5, 363.0,
    #     image = WeatherDescTextBoxImage)

    # WeatherDescTextBoxEntry = Entry(
    #     bd = 0,
    #     bg = "#0b132b",
    #     font = ('Poppins', 16, BOLD),
    #     fg= "#5BC0BE",
    #     justify=CENTER,
    #     highlightthickness = 0)
    # WeatherDescTextBoxEntry.insert(0, weatherData['description'].title())
    # WeatherDescTextBoxEntry.bind("<Key>", lambda e: "break")

    # WeatherDescTextBoxEntry.place(
    #     x = 63, y = 349,
    #     width = 161,
    #     height = 26)


    # TempTextBoxImage = PhotoImage(file = f"./images/home/TempTextBox.png")
    # TempTextBox = canvas.create_image(
    #     417.0, 349.5,
    #     image = TempTextBoxImage)

    # TempTextBoxEntry = Entry(
    #     bd = 0,
    #     bg = "#0b132b",
    #     font = ('Poppins', 13, BOLD),
    #     fg= "#5BC0BE",
    #     justify=RIGHT,
    #     highlightthickness = 0)
    # TempTextBoxEntry.insert(0, weatherData['temp'])
    # TempTextBoxEntry.bind("<Key>", lambda e: "break")

    # TempTextBoxEntry.place(
    #     x = 394, y = 339,
    #     width = 44,
    #     height = 23)



    # FeelsLikeTextBoxImage = PhotoImage(file = f"./images/home/FeelsLikeTextBox.png")
    # FeelsLikeTextBox = canvas.create_image(
    #     435.0, 381.5,
    #     image = FeelsLikeTextBoxImage)
    # uid.append(store.getUID())
    

    # FeelsLikeTextBoxEntry = Entry(
    #     bd = 0,
    #     bg = "#0b132b",
    #     font = ('Poppins', 13, BOLD),
    #     fg= "#5BC0BE",
    #     justify=RIGHT,
    #     highlightthickness = 0)
    # FeelsLikeTextBoxEntry.insert(0, weatherData['feels_like'])
    # FeelsLikeTextBoxEntry.bind("<Key>", lambda e: "break")

    # FeelsLikeTextBoxEntry.place(
    #     x = 408, y = 370,
    #     width = 44,
    #     height = 23)



    # WindTextBoxImage = PhotoImage(file = f"./images/home/WindTextBox.png")
    # WindTextBox = canvas.create_image(
    #     626.0, 369.5,
    #     image = WindTextBoxImage)

    # WindTextBoxEntry = Entry(
    #     bd = 0,
    #     bg = "#0b132b",
    #     font = ('Poppins', 15, BOLD),
    #     fg= "#5BC0BE",
    #     justify=CENTER,
    #     highlightthickness = 0)
    # WindTextBoxEntry.insert(0, weatherData['wind_speed'])
    # WindTextBoxEntry.bind("<Key>", lambda e: "break")

    # WindTextBoxEntry.place(
    #     x = 597, y = 358,
    #     width = 53,
    #     height = 23)

    # HumidityTextBoxImage = PhotoImage(file = f"./images/home/HumidityTextBox.png")
    # HumidityTextBox = canvas.create_image(
    #     904.5, 369.5,
    #     image = HumidityTextBoxImage)

    # HumidityTextBoxEntry = Entry(
    #     bd = 0,
    #     bg = "#0b132b",
    #     font = ('Poppins', 15, BOLD),
    #     fg= "#5BC0BE",
    #     justify=CENTER,
    #     highlightthickness = 0)
    # HumidityTextBoxEntry.insert(0, weatherData['humidity'])
    # HumidityTextBoxEntry.bind("<Key>", lambda e: "break")

    # HumidityTextBoxEntry.place(
    #     x = 895, y = 358,
    #     width = 28,
    #     height = 23)

#####################################################################

    # if len(result) > 0:
    # # # Image for most recent Pdf in database
    #     Pdf1IconImage = PhotoImage(file = f"./images/home/Pdf1Icon.png")
    
    #     Pdf1IconLabel = Button(
    #         canvas,
    #         image = Pdf1IconImage,
    #         borderwidth = 0,
    #         highlightthickness = 0,
    #         background="#1C2541",
    #         activebackground="#1C2541",
    #         command = lambda: toOptionsPage(result[0][0]),
    #         relief = "flat")


    #     Pdf1IconLabel.place(
    #         x = 1057, y = 540,
    #         width = 156,
    #         height = 126)

        
    #     #PDF1 name box
    #     Pdf1TextBoxImage = PhotoImage(file = f"./images/home/TextBox1.png")
    #     Pdf1TextBox = canvas.create_image(
    #         1135.0, 648.0,
    #         image = Pdf1TextBoxImage)

    #     Pdf1Entry = Entry(
    #         bd = 0,
    #         bg = "#1c2541",
    #         font = 20,
    #         fg= "#5BC0BE",
    #         justify=CENTER,
    #         insertbackground= "#1C2541",
    #         highlightthickness = 0)

    #     Pdf1Entry.place(
    #         x = 1057, y = 633,
    #         width = 156,
    #         height = 28)

    #     Pdf1Entry.insert('0' , os.path.basename(result[0][0]))
    #     Pdf1Entry.bind("<Key>", lambda e: "break")

    
    # if len(result) > 1:
    # # # Image for 2nd most recent Pdf in database
    #     Pdf2IconImage = PhotoImage(file = f"./images/home/Pdf2Icon.png")
        
    #     Pdf2IconLabel = Button(
    #         canvas,
    #         image = Pdf2IconImage,
    #         borderwidth = 0,
    #         highlightthickness = 0,
    #         background="#1C2541",
    #         activebackground="#1C2541",
    #         command = lambda: toOptionsPage(result[1][0]),
    #         relief = "flat")

    #     Pdf2IconLabel.place(
    #         x = 1057, y = 374,
    #         width = 156,
    #         height = 126)

    #     #PDF2 name box
    #     Pdf2TextBoxImage = PhotoImage(file = f"./images/home/TextBox2.png")
    #     Pdf2TextBox = canvas.create_image(
    #         1135.0, 648.0,
    #         image = Pdf2TextBoxImage)

    #     Pdf2Entry = Entry(
    #         bd = 0,
    #         bg = "#1c2541",
    #         font = 20,
    #         fg= "#5BC0BE",
    #         justify=CENTER,
    #         insertbackground= "#1C2541",
    #         highlightthickness = 0)

    #     Pdf2Entry.place(
    #         x = 1057, y = 467,
    #         width = 156,
    #         height = 28)

    #     Pdf2Entry.insert('0' , os.path.basename(result[1][0]))
    #     Pdf2Entry.bind("<Key>", lambda e: "break")

    # if len(result) > 2:
    # # # Image for 3rd most recent Pdf in database
    #     Pdf3IconImage = PhotoImage(file = f"./images/home/Pdf3Icon.png")
        
    #     Pdf3IconLabel = Button(
    #         canvas,
    #         image = Pdf3IconImage,
    #         borderwidth = 0,
    #         highlightthickness = 0,
    #         background="#1C2541",
    #         activebackground="#1C2541",
    #         command =lambda: toOptionsPage(result[2][0]),
    #         relief = "flat")


    #     Pdf3IconLabel.place(
    #         x = 1057, y = 208,
    #         width = 156,
    #         height = 126)

    #     #PDF3 name box
    #     Pdf3TextBoxImage = PhotoImage(file = f"./images/home/TextBox3.png")
    #     Pdf2TextBox = canvas.create_image(
    #         1135.0, 648.0,
    #         image = Pdf3TextBoxImage)

    #     Pdf3Entry = Entry(
    #         bd = 0,
    #         bg = "#1c2541",
    #         font = 20,
    #         fg= "#5BC0BE",
    #         justify=CENTER,
    #         insertbackground= "#1C2541",
    #         highlightthickness = 0)

    #     Pdf3Entry.place(
    #         x = 1057, y = 301,
    #         width = 156,
    #         height = 28)

    #     Pdf3Entry.insert('0' , os.path.basename(result[2][0]))
    #     Pdf3Entry.bind("<Key>", lambda e: "break")



    # if len(result) == 0:
    #     # Image for 3rd most recent Pdf in database
    #     NotFoundImage = PhotoImage(file = f"./images/home/notFound.png")
        
    #     NotFoundLabel = Label(
    #         image = NotFoundImage,
    #         background="#1C2541",
    #         activebackground="#1C2541"
    #     )


    #     NotFoundLabel.place(
    #         x = 1042, y = 250,
    #         width = 176,
    #         height = 231)

    