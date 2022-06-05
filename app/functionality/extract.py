import PyPDF2

#function to extract text from pdf file copy it to a txt file
def extract(file):
    #opening the pdf and text files
    pdf = open(file, 'rb')
    tf=open('output.txt','wt')

    # creating an pages variables and assigning it to an empty string
    Pages=''

    #pdf reader obj
    pdfReader = PyPDF2.PdfFileReader(pdf)
    
    page=pdfReader.getPage(1)
    #adding pages to pdf reader obj and extracting the text to a variable
    for pageNo in range(pdfReader.numPages):
        Page = pdfReader.getPage(pageNo)
        page=Page.extractText()
        Pages+=page
   
    #copying the text from the variable to a text file
    tf.write(Pages)

    #save the changes and closing the files
    tf.close()
    pdf.close()

    #checking if the text is empty
    if Pages.strip()=='':
        return True
    else:
        return False 
