import PyPDF2

# this function is used to decrypt the pdf file
# parameters and the name of the file to be decrypted and the password
def encrypt(file_name, password):
    # opening the file in read mode
    openFile = open(file_name, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(openFile)
    # creating a pdf writer object
    pdfWriter = PyPDF2.PdfFileWriter()
    # looping through the pages of the pdf file
    for page in range(pdfReader.numPages):
        # getting all the individual pages
        newPage = pdfReader.getPage(page)
        # adding the pages to the writer object buffer
        pdfWriter.addPage(newPage)
    # encrypting the page
    pdfWriter.encrypt(password)
    # creating a new file
    outFile = open("encrypted.pdf", "wb")
    # writing the encrypted file to the new file
    pdfWriter.write(outFile)
    # closing the files
    openFile.close()
    outFile.close()
