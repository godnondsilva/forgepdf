import PyPDF2

# merge pdf function
def merge(pdfList):
    # if no files are entered
    if len(pdfList) == 0:
        return "Enter Atleast 2 pdf files"
    # checking whether more than 3 pdf files have entered
    elif len(pdfList) > 3:
        return "Maximum Of 3 Pdf Files Are Allowed"
    # if above 2 condition is false continue with the following
    else:
        pdfWriter = PyPDF2.PdfFileWriter()
        newFile = open("Merge.pdf", 'wb')
        for pdfCount in range(len(pdfList)):
            # checking whether the inputted files are only pdf
            if pdfList[pdfCount].endswith('.pdf') == False:
                return "Input Only Pdf Files..."
            else:
                file = open(pdfList[pdfCount], 'rb')
                pdfReader = PyPDF2.PdfFileReader(file)

                for page in range(pdfReader.numPages):
                    newPage = pdfReader.getPage(page)
                    pdfWriter.addPage(newPage)
                pdfWriter.write(newFile)
                file.close()
    newFile.close()
    return "Files Got Merged!!"
