import PyPDF2,os.path   

# funtion to split pdf file into multiple pdf files
def spliter(start,end, file):
    #opening the input and output pdf files
    pdfFile=open(file,'rb')
    outputFile=open('output.pdf','wb')
  
    #creating the pdfreader and pdfwriter objects to read and write from and to pdf files
    pdfReader=PyPDF2.PdfFileReader(pdfFile)
    pdfWriter=PyPDF2.PdfFileWriter()

    #adding pages to the pdfwriter object
    try:
        for pageNo in range(start-1,end):
            page = pdfReader.getPage(pageNo)
            pdfWriter.addPage(page)
    #if the page range added are not in range of pdf
    except: 
            #closing the pdfs in case of error
            outputFile.close()
            pdfFile.close()
            return False


    #writing the pages stored in pdfwriter to output pdf
    pdfWriter.write(outputFile)      

    #closing the pdfs 
    outputFile.close()
    pdfFile.close()
    return True
