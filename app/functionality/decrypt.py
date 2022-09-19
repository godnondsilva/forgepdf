import PyPDF2

def decrypt(file, password):
    # Opening the encrypted file and decrypted file in read and write mode respectively
    encrypted_file = open(file, 'rb')
    decrypted_file= open('output.pdf', 'wb')

    pdf_reader = PyPDF2.PdfFileReader(encrypted_file)
    pdf_writer = PyPDF2.PdfFileWriter()

    isEncrypted = pdf_reader.isEncrypted
    if isEncrypted == 0:
        encrypted_file.close()
        decrypted_file.close()
        return {
            'status': 'error',
            'message': 'The file is not encrypted.'
        }

    isPasswordValid = pdf_reader.decrypt(password)
    if isPasswordValid == 0:
        encrypted_file.close()
        decrypted_file.close()
        return {
            'status': 'error',
            'message': 'The password is incorrect.'
        }
    
    # Copying the pages from the encrypted file to the writer object
    for page_no in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_no)
        pdf_writer.addPage(page)

    # Write the decrypted file to the disk
    pdf_writer.write(decrypted_file)

    # Saving the changes and closing the files
    encrypted_file.close()
    decrypted_file.close()

    # Returning the status and message
    return {
        'status': 'success',
        'message': 'The file has been decrypted successfully'
    }
