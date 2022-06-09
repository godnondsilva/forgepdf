from tkinter import *
from tkinter import filedialog
import mysql.connector
from app import home,options
from app import store
from app.utility import center
import os

class SavedPdfWindow():
     def __init__(self):
        # window config
        window = Tk()
        window.geometry("1280x720")
        window.title('ForgePDF | Saved PDFs')
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

        #Route to options page and store the selected pdf
        def toOptionsPage(SelectPdf):
            #set the value in the user details class
            store.setSelectPdf(SelectPdf)

            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the options up window class
            options.OptionsPdfWindow()


        canvas = Canvas(
            window,
            bg = "#0b132b",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        #SavedPDF BG Config
        SavedPdfBGImage = PhotoImage(file = f"./images/savedpdfs/SavedPdfBG.png")
        SavedPDfBG = canvas.create_image(
            640.0, 124.0,
            image=SavedPdfBGImage)

        #Back Button Config
        BackImage = PhotoImage(file = f"./images/savedpdfs/Back.png")
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



        #gettting the current logged in user's id
        uid.append(store.getUID())
        
        # creating a mysql connection
        mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database="forgepdf")
        mycursor = mydb.cursor()
        # getting all the user data from the database
        mycursor.execute("select file_address from files where user_id='" + str(uid[0]) + "' order by file_id desc")
        # selecting only the first row from the fetched data
        result = mycursor.fetchall()
        print(result)


        if len(result) > 0:
            #Pdf1 Button Config
            Pdf1Icon = PhotoImage(file = f"./images/savedpdfs/Pdf1.png")
            Pdf1Button = Button(
                image = Pdf1Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command = lambda: toOptionsPage(result[0][0]),
                relief = "flat")

            Pdf1Button.place(
                x = 111, y = 281,
                width = 90,
                height = 98)

            #Pdf1 Text Config
            TextBox1EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox1.png")
            TextBox1Entry = canvas.create_image(
                156.0, 411.5,
                image = TextBox1EntryImage)

            TextBox1 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)
            
            TextBox1.insert('0' , os.path.basename(result[0][0]))
            TextBox1.bind("<Key>", lambda e: "break")

            TextBox1.place(
                x = 63, y = 395,
                width = 186,
                height = 31)



        if len(result) > 1:
            #Pdf2 Button Config
            Pdf2Icon = PhotoImage(file = f"./images/savedpdfs/Pdf2.png")
            Pdf2Button = Button(
                image = Pdf2Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command =lambda: toOptionsPage(result[1][0]),
                relief = "flat")

            Pdf2Button.place(
                x = 111, y = 499,
                width = 90,
                height = 98)

            
            #Pdf2 Entry Box Config
            TextBox2EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox2.png")
            TextBox2Entry = canvas.create_image(
                156.0, 629.5,
                image = TextBox2EntryImage)

            TextBox2 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)

            TextBox2.insert('0' , os.path.basename(result[1][0]))
            TextBox2.bind("<Key>", lambda e: "break")

            TextBox2.place(
                x = 63, y = 613,
                width = 186,
                height = 31)




        if len(result) > 2:
            #PDF3 Button Config
            Pdf3Icon = PhotoImage(file = f"./images/savedpdfs/Pdf3.png")
            Pdf3Button = Button(
                image = Pdf3Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command= lambda: toOptionsPage(result[2][0]),
                relief = "flat")

            Pdf3Button.place(
                x = 297, y = 281,
                width = 90,
                height = 98)

            #PDF3 Entry config
            TextBox3EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox3.png")
            TextBox3Entry = canvas.create_image(
                342.0, 411.5,
                image = TextBox3EntryImage)

            TextBox3 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)

            TextBox3.insert('0' , os.path.basename(result[2][0]))
            TextBox3.bind("<Key>", lambda e: "break")

            TextBox3.place(
                x = 249, y = 395,
                width = 186,
                height = 31)


        if len(result) > 3:
            #PDF4 Button Config
            Pdf4Icon = PhotoImage(file = f"./images/savedpdfs/Pdf4.png")
            Pdf4Button = Button(
                image = Pdf4Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command = lambda: toOptionsPage(result[3][0]),
                relief = "flat")

            Pdf4Button.place(
                x = 297, y = 499,
                width = 90,
                height = 98)

            
            #PDF4 Entry Config
            TextBox4EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox4.png")
            TextBox4Entry = canvas.create_image(
                342.0, 629.5,
                image = TextBox4EntryImage)

            TextBox4 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)

            TextBox4.insert('0' , os.path.basename(result[3][0]))
            TextBox4.bind("<Key>", lambda e: "break")

            TextBox4.place(
                x = 249, y = 613,
                width = 186,
                height = 31)



        if len(result) > 4:
            #PDf5 Button Config
            Pdf5Icon = PhotoImage(file = f"./images/savedpdfs/Pdf5.png")
            Pdf5Button = Button(
                image = Pdf5Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command = lambda: toOptionsPage(result[4][0]),
                relief = "flat")

            Pdf5Button.place(
                x = 483, y = 281,
                width = 90,
                height = 98)

            #Pdf5 TextBox Config
            TextBox5EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox5.png")
            TextBox5Entry = canvas.create_image(
                528.0, 411.5,
                image = TextBox5EntryImage)

            TextBox5 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)

            TextBox5.insert('0' , os.path.basename(result[4][0]))
            TextBox5.bind("<Key>", lambda e: "break")

            TextBox5.place(
                x = 435, y = 395,
                width = 186,
                height = 31)


        if len(result) > 5:
            #PDF6 Icon Config
            Pdf6Icon = PhotoImage(file = f"./images/savedpdfs/Pdf6.png")
            Pdf6Button = Button(
                image = Pdf6Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command = lambda: toOptionsPage(result[5][0]),
                relief = "flat")

            Pdf6Button.place(
                x = 483, y = 499,
                width = 90,
                height = 98)

            #Pdf6 Entry Config
            TextBox6EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox6.png")
            TextBox6Entry = canvas.create_image(
                528.0, 629.5,
                image = TextBox6EntryImage)

            TextBox6 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)

            TextBox6.insert('0' , os.path.basename(result[5][0]))
            TextBox6.bind("<Key>", lambda e: "break")

            TextBox6.place(
                x = 435, y = 613,
                width = 186,
                height = 31)



        if len(result) > 6:
            #Pdf7 Icon
            Pdf7Icon = PhotoImage(file = f"./images/savedpdfs/Pdf7.png")
            Pdf7Button = Button(
                image = Pdf7Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command = lambda: toOptionsPage(result[6][0]),
                relief = "flat")

            Pdf7Button.place(
                x = 669, y = 281,
                width = 90,
                height = 98)

            #Pdf7 Entry
            TextBox7EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox7.png")
            TextBox7Entry = canvas.create_image(
                714.0, 411.5,
                image = TextBox7EntryImage)

            TextBox7 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)

            TextBox7.insert('0' , os.path.basename(result[6][0]))
            TextBox7.bind("<Key>", lambda e: "break")

            TextBox7.place(
                x = 621, y = 395,
                width = 186,
                height = 31)


        if len(result) > 7:
            #Pdf8 Icon
            Pdf8Icon = PhotoImage(file = f"./images/savedpdfs/Pdf8.png")
            Pdf8Button = Button(
                image = Pdf8Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command = lambda: toOptionsPage(result[7][0]),
                relief = "flat")

            Pdf8Button.place(
                x = 669, y = 499,
                width = 90,
                height = 98)

            #Pdf8 Entry
            TextBox8EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox8.png")
            TextBox8Entry = canvas.create_image(
                714.0, 629.5,
                image = TextBox8EntryImage)

            TextBox8 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)

            TextBox8.insert('0' , os.path.basename(result[7][0]))
            TextBox8.bind("<Key>", lambda e: "break")

            TextBox8.place(
                x = 621, y = 613,
                width = 186,
                height = 31)


        if len(result) > 8:
            #Pdf9 Icon
            Pdf9Icon = PhotoImage(file = f"./images/savedpdfs/Pdf9.png")
            Pdf9Button = Button(
                image = Pdf9Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command = lambda: toOptionsPage(result[8][0]),
                relief = "flat")

            Pdf9Button.place(
                x = 855, y = 281,
                width = 90,
                height = 98)

            #Pdf9 Entry
            TextBox9EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox8.png")
            TextBox9Entry = canvas.create_image(
                900.0, 411.5,
                image = TextBox9EntryImage)

            TextBox9 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)

            TextBox9.insert('0' , os.path.basename(result[8][0]))
            TextBox9.bind("<Key>", lambda e: "break")

            TextBox9.place(
                x = 807, y = 395,
                width = 186,
                height = 31)



        if len(result) > 9:
            #Pdf10 Icon
            Pdf10Icon = PhotoImage(file = f"./images/savedpdfs/Pdf10.png")
            Pdf10Button = Button(
                image = Pdf10Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command = lambda: toOptionsPage(result[9][0]),
                relief = "flat")

            Pdf10Button.place(
                x = 855, y = 499,
                width = 90,
                height = 98)

            #Pdf10 Entry
            TextBox10EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox10.png")
            TextBox10Entry = canvas.create_image(
                900.0, 629.5,
                image = TextBox10EntryImage)

            TextBox10 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)


            TextBox10.insert('0' , os.path.basename(result[9][0]))
            TextBox10.bind("<Key>", lambda e: "break")

            TextBox10.place(
                x = 807, y = 613,
                width = 186,
                height = 31)

        

        if len(result) > 10:
            #Pdf11 Icon
            Pdf11Icon = PhotoImage(file = f"./images/savedpdfs/Pdf11.png")
            Pdf11Button = Button(
                image = Pdf10Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command = lambda: toOptionsPage(result[10][0]),
                relief = "flat")

            Pdf11Button.place(
                x = 1045, y = 281,
                width = 90,
                height = 98)


            #Pdf11 Entry
            TextBox11EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox11.png")
            TextBox11Entry = canvas.create_image(
                1090.0, 411.5,
                image = TextBox11EntryImage)

            TextBox11 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)

            TextBox11.insert('0' , os.path.basename(result[10][0]))
            TextBox11.bind("<Key>", lambda e: "break")

            TextBox11.place(
                x = 997, y = 395,
                width = 186,
                height = 31)



        if len(result) > 11:
            #Pdf12 Icon
            Pdf12Icon = PhotoImage(file = f"./images/savedpdfs/Pdf12.png")
            Pdf12Button = Button(
                image = Pdf12Icon,
                borderwidth = 0,
                highlightthickness = 0,
                background="#0B132B",
                activebackground="#0B132B",
                command = lambda: toOptionsPage(result[11][0]),
                relief = "flat")

            Pdf12Button.place(
                x = 1045, y = 499,
                width = 90,
                height = 98)

            
            #Pdf12 Entry
            TextBox12EntryImage = PhotoImage(file = f"./images/savedpdfs/TextBox12.png")
            TextBox12Entry = canvas.create_image(
                1090.0, 629.5,
                image = TextBox12EntryImage)

            TextBox12 = Entry(
                bd = 0,
                bg = "#0b132b",
                font = 20,
                fg= "#5BC0BE",
                justify=CENTER,
                insertbackground= "#0B132B",
                highlightthickness = 0)

            TextBox12.insert('0' , os.path.basename(result[11][0]))
            TextBox12.bind("<Key>", lambda e: "break")

            TextBox12.place(
                x = 997, y = 613,
                width = 186,
                height = 31)


        if len(result) == 0:
            #Image if no files are found in database
            NotFoundImage = PhotoImage(file = f"./images/savedpdfs/notFound.png")
            
            NotFoundLabel = Label(
                image = NotFoundImage,
                background="#0B132B",
                activebackground="#0B132B"
            )

            NotFoundLabel.place(
                x = 500, y = 300,
                width = 176,
                height = 231)


        
        #Additional window config
        window.resizable(False, False)
        window.iconbitmap('images/logo.ico')
        window.deiconify()
        window.mainloop()
