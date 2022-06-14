import csv, os

# Function to send email
def send_email(toaddress , attachmentPath):
    pass

# Function to extract email addresses from a csv file
def csvToStr(adrresses ,attachmentPath):
    address =''
    file= open(adrresses)
    eaddr=list(csv.reader(file))
    print(eaddr)
    for i in range(len(eaddr[0])):
        print(eaddr[0][i])
        address+=eaddr[0][i]+','
    # return address

    print(address , attachmentPath)

