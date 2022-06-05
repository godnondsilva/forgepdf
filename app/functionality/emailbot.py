from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv,os

def emailbot(toaddress , attachmentPath):#used to send email
    #converting relative path of the attachment to absolute path
    web = webdriver.Chrome()
    web.maximize_window()#make the window full screen

    #opening the gmail login page in chrome
    web.get('https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    
    #getting the email address textbox and inserting the email address in it
    email=web.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
    email.send_keys(os.getenv('SELENIUM_EMAIL')+ Keys.ENTER)    
    
    #waiting for the password page to load
    web.implicitly_wait(500)

    #getting the password textbox and inserting the password in it
    pwd=web.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    pwd.send_keys(os.getenv('SELENIUM_PASSWORD')+ Keys.ENTER)  

    #waiting for the page to load
    web.implicitly_wait(1000)

    #pressing the compose button to create a new email
    web.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div').click()
    
    web.implicitly_wait(1000)
    
    #getting the  to textbox and inserting the to email address in it
    toadd=web.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/textarea')
    toadd.send_keys(toaddress)
    
    web.implicitly_wait(1000)

    #getting the subject textbox and inserting the subject in it
    subject=web.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/div/input')
    subject.send_keys('FORGEPDF')    

    #getting the attachment from the path variable and attaching it to the email 
    attachment=web.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[4]/div/input')
    attachment.send_keys(attachmentPath)

    print("Added attachment")
    
    web.implicitly_wait(1000)

    #finding the send button and clicking it to send the email
    web.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]').click()  
    
    #waiting for the message sent popup
    web.implicitly_wait(1000)

    #checking for the message sent popup
    web.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[4]/div[1]/div/div[3]/div/div/div[2]/span/span[2]/span[2]')
    
    #clicking on the user dp
    web.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[3]/div[1]/div[2]/div/a').click()
   
    #clicking on the signout button
    web.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[4]/div[4]/a').click()


def csvToStr(adrresses ,attachmentPath):#function to extract email addresses from a csv file
    address =''
    file= open(adrresses)
    eaddr=list(csv.reader(file))
    print(eaddr)
    for i in range(len(eaddr[0])):
        print(eaddr[0][i])
        address+=eaddr[0][i]+','
    # return address

    print(address , attachmentPath)
    emailbot(address , attachmentPath)

