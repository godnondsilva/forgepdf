#Stores the current users id ,selectedpdf and name here
from ntpath import join


uid = []
username = []
selectPdf = []
Currentcount = [0]

#function to SET the UID of the user who logged in
def setUID(useruid):
    if len(uid) == 0:
        uid.append(useruid)
    else:
        uid[0] = useruid


#fucntion to get the UID of the user who is already logged in
def getUID():
    return uid[0]



#function to SET the name of the user who logged in
def setUsername(userName):
    if len(username) == 0:
        username.append(userName)
    else:
        username[0] = userName


#function to get the UID of the user who is already logged in
def getUsername():
    return username[0]


#function to SET the pdf user selected
def setSelectPdf(Pdfaddress):
    if len(selectPdf) == 0:
        selectPdf.append(Pdfaddress)
    else:
        selectPdf[0] = Pdfaddress


#function to get the pdf the user selected
def getSelectPdf():
    return selectPdf[0]



#checks if the email , split , merge pdf where reached by options page or not
hasSelectpdf = [False]

def SetSelectedPdfBool():
    hasSelectpdf[0] = True

def GetselectedPdfBool():
    return hasSelectpdf[0]

def NotSelectPdfBool():
    hasSelectpdf[0] = False


#Increments the count of the pdfs
def IncrementCount():
    Currentcount[0]+=1


#gets the count of the pdf
def getCount():
    return Currentcount[0]

#gets the count from DB
def SetCount(count):
    Currentcount[0] = count

#converts the address to a form which can be saved in DB
def ConvertAddress(add):
    lsit = add.split('\\')
    print(lsit)
    newadd = '/'.join(lsit)
    print(newadd)
    return newadd
