import PyPDF2

def spliter(start,end, file):
    # Opening the input and output pdf files
    pdfFile=open(file,'rb')
    outputFile=open('output.pdf','wb')
  
    # Creating the pdfreader and pdfwriter objects to read and write from and to pdf files
    pdfReader=PyPDF2.PdfFileReader(pdfFile)
    pdfWriter=PyPDF2.PdfFileWriter()

    # Adding pages to the pdfwriter object
    try:
        for pageNo in range(start-1,end):
            page = pdfReader.getPage(pageNo)
            pdfWriter.addPage(page)
    # If the page range added are not in range of pdf
    except: 
            # Closing the pdfs in case of error
            outputFile.close()
            pdfFile.close()
            return {
                "status": "error",
                "message": "Page range not in range of pdf"
            }


    # Writing the pages stored in pdfwriter to output pdf
    pdfWriter.write(outputFile)      

    # Closing the pdfs 
    outputFile.close()
    pdfFile.close()
    return {
        'status': 'success',
        'message': 'File split successfully'
    }
