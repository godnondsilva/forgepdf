from tkinter import *
from tkinter.messagebox import showwarning, showerror
from app import login , home
from app.functionality import scrapping, inputValidation
from app.utility import center
import threading, shutil

class ScrapyWindow  ():
    def __init__(self):
        #Window config
        window = Tk()
        window.geometry("1280x720")
        window.title('ForgePDF | Scrapy')
        center(window)
        window.configure(bg = "#0b132b")

        #Button Functions
        def toHomePage():
            # destroy the current window instance (LogInWindow)
            window.destroy()
            # call the login up window class
            home.HomeWindow()
        
        def handleStart():
            try:
                #getting the input from the text box
                itemToScrap = InputEntry.get()
                new_item = itemToScrap.strip()

                condition = inputValidation.scrappyVal(new_item)
                if condition != True:
                    showwarning('Error', condition['error'])
                else:
                    handleThread()
            except:
                showerror("Error" , "An error has occurred!")
                window.destroy()
                home.HomeWindow()
        
        #Moves the files to desktop
        def MoveToDesktop():
            add = 'C:\\Users\\User\\Desktop\\productListFile.csv'
            shutil.move('productListFile.csv' , add)

        def handleThread():
            threading.Timer(0.1, ScrapIt).start()
            threading.Timer(0.1, showLoading).start()
            threading.Timer(10.0, showDone).start()

        def ScrapIt():
            itemToScrap = InputEntry.get()
            #call the scrapping function and scrap the details
            isDone = scrapping.main(itemToScrap)
            if isDone:
                MoveToDesktop()


        #Shows the loading label when the button is pressed
        def showLoading():
            # ScrapItButton.pack_forget()
            ScrapItLoadingLabel.pack()
            ScrapItLoadingLabel.place(  
            x = 362, y = 557,
            width = 536,
            height = 100)
        
        #shows the done label 5 seconds after the button is pressed
        def showDone():
            # ScrapItLoadingButton.pack_forget()
            ScrapItDoneLabel.pack()
            ScrapItDoneLabel.place(  
            x = 362, y = 557,
            width = 536,
            height = 100)

            
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


        #Scrapy Background config
        ScrapyBGImage = PhotoImage(file = f"./images/Scrapy/ScrapyBG.png")
        ScrapyBG = canvas.create_image(
            640.0, 155.5,
            image=ScrapyBGImage)

        #Scrapy Button Config
        ScrapitImage = PhotoImage(file = f"./images/Scrapy/Scrapit.png")
        ScrapItButton = Button(
            image = ScrapitImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",

            #creating 3 threads to run the scraping , and show the 2 labels at some fixed time
            command= handleStart,
            relief = "flat")

        ScrapItButton.place(
            x = 362, y = 557,
            width = 536,
            height = 100)
        

        #Loading Image Config
        ScrapItLoadingImage = PhotoImage(file = f"./images/Scrapy/LoadingImage.png")
        ScrapItLoadingLabel = Label(
            image = ScrapItLoadingImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            relief = "flat")
   
        #packing the label and hiding it 
        ScrapItLoadingLabel.pack()
        ScrapItLoadingLabel.pack_forget()



        #Done Image Config
        ScrapItDoneImage = PhotoImage(file = f"./images/Scrapy/DoneImage.png")
        ScrapItDoneLabel = Label(
            image = ScrapItDoneImage,
            borderwidth = 0,
            highlightthickness = 0,
            background="#0B132B",
            activebackground="#0B132B",
            relief = "flat")


        ScrapItDoneLabel.place(  
            x = 362, y = 557,
            width = 536,
            height = 100)
        
        #packing the label and hiding it 
        ScrapItDoneLabel.pack()
        ScrapItDoneLabel.pack_forget()



        #back button config
        BackImage = PhotoImage(file = f"./images/Scrapy/Back.png")
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



        #Input entry config
        InputEntryImage = PhotoImage(file = f"./images/Scrapy/TextBox.png")
        InputEntry = canvas.create_image(
            639.5, 391.5,
            image = InputEntryImage)

        InputEntry = Entry(
            bd = 0,
            bg = "#1c2541",
            font = 30,
            fg= "#5BC0BE",
            justify=CENTER,
            insertbackground= "#5BC0BE",
            highlightthickness = 0)

        InputEntry.place(
            x = 282, y = 360,
            width = 715,
            height = 61)

        # additional window config
        window.resizable(False, False)
        window.iconbitmap('images/logo.ico')
        window.deiconify()
        window.mainloop()
