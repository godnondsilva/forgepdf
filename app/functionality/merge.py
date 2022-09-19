import PyPDF2

def merge(pdf_list):
    pdf_writer = PyPDF2.PdfFileWriter()
    merged_file = open("output.pdf", 'wb')

    for pdfCount in range(len(pdf_list)):
        # Checking whether the inputted files are only pdf
        if pdf_list[pdfCount].endswith('.pdf') == True:
            file_to_merge = open(pdf_list[pdfCount], 'rb')
            pdfReader = PyPDF2.PdfFileReader(file_to_merge)

            # looping through the pages of the pdf file_to_merge
            for page in range(pdfReader.numPages):
                newPage = pdfReader.getPage(page)
                pdf_writer.addPage(newPage)
                
    pdf_writer.write(merged_file)
    file_to_merge.close()
    merged_file.close()
    return {
        "status": "success",
        "message": "PDF files are merged"
    }
