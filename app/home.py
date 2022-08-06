from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror
from tkinter.font import BOLD
from app import login, encryptpdf, sidebar
from app.store import state, states
from app import store
from app.functionality import weather, thought
from app.utility import execute_query_fetch_all
import datetime, os

import threading

def load_home(window):
    #Button Functions
    class WeatherThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
    
            # helper function to execute the threads
        def run(self):
            weatherData = weather.get_weather(state.get_state(states.LOCATION))
            if 'error' in weatherData:
                showerror('Error', weatherData['error'])
            # Description text
            description_entry.insert(0, "Feels like " + str(int(weatherData['temp'])) + "°C. " + weatherData['main'].capitalize() + ". " + str(weatherData['description']).capitalize())
            description_entry.bind("<Key>", lambda e: "break")

            # Temperature text
            temperature_entry.insert(0, str(int(weatherData['temp'])) + "°C")
            temperature_entry.bind("<Key>", lambda e: "break")

            # Humidity text
            humidity_entry.insert(0, "Humidity: " + str(int(weatherData['temp'])) + "%")
            humidity_entry.bind("<Key>", lambda e: "break")

            # Wind text
            wind_entry.insert(0, "Wind: " + str(int(weatherData['temp'])) + "km/hr")
            wind_entry.bind("<Key>", lambda e: "break")

            # Pressure text
            pressure_entry.insert(0, "Pressure: " + str(int(weatherData['temp'])) + "Pa")
            pressure_entry.bind("<Key>", lambda e: "break")

    class ThoughtThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
         # helper function to execute the threads
        def run(self):
            thought_text_value = thought.get_thought()
            thought_text.delete(1.0, END)
            thought_text.insert(END, thought_text_value)
            thought_text.config(state=DISABLED)

    def logout():
        # Reset the state
        state.reset_state()
        # route to the login frame
        login.load_login(window)

    # def route_decrypt_pdf():
    #     # call the decrypt pdf window class
    #     decryptpdf.decryptWindow()

    # def route_email_pdf():
    #     # call the email pdf window class
    #     emailpdf.EmailPdfWindow()

    # def route_extract_pdf():
    #     # call the extract pdf window class
    #     extractpdf.extractWindow()


    # def route_split_pdf():
    #     # call the splitPdf window class
    #     splitpdf.SplitPdfWIndow()
        
    # def route_merge_pdf():
    #     # call the merge pdf window class
    #     mergepdf.MergePdfWindow()

    # def route_saved_pdf():
    #     # call the saved pdf window class
    #     savedpdfs.SavedPdfWindow()


    # def route_options(SelectPdf):
    #     #set the value of the pdf select by the user in the user details class
    #     store.setSelectPdf(SelectPdf)
    #     # call the options up window class
    #     options.OptionsPdfWindow()
    
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

    background_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/background.png")
    background_label = Label(image=background_img)
    background_label.image = background_img
    background = canvas.create_image(
        671.0, 384.0,
        image=background_img)

    logout_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/logout_btn.png")
    logout_btn_label = Label(image=logout_btn_img)
    logout_btn_label.image = logout_btn_img
    logout_btn = Button(
        image = logout_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        background="#111111",
        activebackground="#111111",
        command = logout,
        relief = "flat")

    logout_btn.place(
        x = 1111, y = 35,
        width = 160,
        height = 45)

    sidebar.load_sidebar(window)

    send_bug_report_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/send_bug_report_btn.png")
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

    send_feedback_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/send_feedback_btn.png")
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

    view_more_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/view_more_btn.png")
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

    empty_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/empty.png")
    empty_label = Label(image = empty_img, bg = "#333333")
    empty_label.image = empty_img
    empty_label.place(
        x = 544, y = 590,
        width = 528,
        height = 50)
    
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

    datetime_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/datetime_entry.png")
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
        width = 120,
        height = 19)

    location_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/location_entry.png")
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

    weather_btn_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/weather_btn.png")
    weather_btn_label = Label(
        image=weather_btn_img,
        bg="#333333",
        activebackground="#333333")
    weather_btn_label.image = weather_btn_img

    weather_btn_label.place(
        x = 860, y = 196,
        width = 63,
        height = 55)

    # TODO: Change the weather icon based on the current weather
    sunny_image_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/sunny.png")
    weather_btn_label.config(image = sunny_image_img)
    weather_btn_label.image = sunny_image_img

    temperature_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/temperature_entry.png")
    temperature_entry_bg = canvas.create_image(
        979.0, 223.5,
        image = temperature_entry_img)

    temperature_entry = Entry(
        bd = 0,
        font=("Poppins", 26),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#333333")

    temperature_entry.place(
        x = 929, y = 196,
        width = 100,
        height = 53)

    description_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/description_entry.png")
    description_entry_bg = canvas.create_image(
        1006.5, 278.0,
        image = description_entry_img)

    description_entry = Entry(
        bd = 0,
        font=("Poppins", 10),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#333333")
    
    description_entry.place(
        x = 860, y = 268,
        width = 271,
        height = 18)

    wind_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/wind_entry.png")
    wind_entry_bg = canvas.create_image(
        935.5, 349.0,
        image = wind_entry_img)

    wind_entry = Entry(
        bd = 0,
        font=("Poppins", 10),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#5a5a5a")

    wind_entry.place(
        x = 875, y = 338,
        width = 99,
        height = 20)

    humidity_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/humidity_entry.png")
    humidity_entry_bg = canvas.create_image(
        941.5, 324.0,
        image = humidity_entry_img)

    humidity_entry = Entry(
        bd = 0,
        font=("Poppins", 10),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#5a5a5a")

    humidity_entry.place(
        x = 875, y = 313,
        width = 111,
        height = 20)

    pressure_entry_img = PhotoImage(file = os.getenv("IMAGE_FOLDER_PATH")+"/home/pressure_entry.png")
    pressure_entry_bg = canvas.create_image(
        939.0, 374.0,
        image = pressure_entry_img)

    pressure_entry = Entry(
        bd = 0,
        font=("Poppins", 10),
        highlightthickness = 0, 
        borderwidth=0,
        fg= "#FFFFFF",
        bg = "#5a5a5a")

    pressure_entry.place(
        x = 875, y = 363,
        width = 106,
        height = 20)

    # Configuration
    # Weather API call
    weather_thread = WeatherThread()
    weather_thread.start()

    # Thought text
    thought_text.insert(END, "Loading...")
    thought_thread = ThoughtThread()
    thought_thread.start()

    # Name text
    name_text_value = state.get_state(states.USERNAME)
    if 'error' in name_text_value:
        showerror('Error', name_text_value['error'])
    name_text.insert(END, "Welcome, "+name_text_value.title())
    name_text.config(state=DISABLED)

    # Datetime text
    datetime_entry.insert(0, datetime.date.today().strftime("%A") + ', ' + datetime.datetime.now().strftime("%I:%M %p"))
    datetime_entry.bind("<Key>", lambda e: "break")

    # Location text
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

    # result = execute_query_fetch_all("select file_address from files where user_id='" + str(store.getUID()) + "' order by file_id desc")

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


    # #####################################################################

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

    