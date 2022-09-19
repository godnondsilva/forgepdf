import PyPDF2

def encrypt(file_name, password):
    file_to_encrypt = open(file_name, 'rb')

    # Creating a pdf reader and writer objects
    pdfReader = PyPDF2.PdfFileReader(file_to_encrypt)
    pdfWriter = PyPDF2.PdfFileWriter()

    # looping through the pages of the pdf file
    for page in range(pdfReader.numPages):
        new_page = pdfReader.getPage(page)
        pdfWriter.addPage(new_page)

    # Encrypting the page
    pdfWriter.encrypt(password)

    # Opening and riting the encrypted file to the new file
    encrypted_file = open("output.pdf", "wb")
    pdfWriter.write(encrypted_file)

    # Closing the files
    file_to_encrypt.close()
    encrypted_file.close()

    return {
        'status': 'success',
        'message': 'PDF encrypted successfully'
    }
