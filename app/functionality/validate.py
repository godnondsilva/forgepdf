import re

# Function to check whether the string given is containing only numbers
def validate_split(start, end):
    # The variables start and end are string variables
    # Convert to int for comparing values
    # If starting range is greater than endingrange
    if (int(start) > int(end)):
        return {
            "status": "error",
            "message": "Starting range cannt be greater than ending range!"
        }
    if start.isdecimal()==False and end.isdecimal()==False:
        return {
            "status": "error",
            "message": "Please enter a valid range"
        }
    else:
        return {
            "status": "success",
            "message": "Range is valid"
        }


# function for validating the inputs from encrypt pdf page
# validates the password field
def validate_encrypt(password):
    # if the password is empty
    if len(password) == 0:
        return {
            "status": "error",
            "message": "Please enter a valid password"
        }
    else:
        return {
            "status": "success",
            "message": "Password is valid"
        }

# function for validating the inputs from decrypt pdf page
# validates the password field
def validate_decrypt(password):
    # if the password is empty
    if len(password) == 0:
        return {
            "status": "error",
            "message": "Please enter a valid password"
        }
    else:
        return {
            "status": "success",
            "message": "Password is valid"
        }

# function for validating the merge pdf function
def validate_merge(pdf_list):
    if len(pdf_list) == 0:
        return {
            "status": "error",
            "message": "Please select atleast one pdf file"
        }
    # checking whether more than 3 pdf files have entered
    elif len(pdf_list) > 5:
        return {
            "status": "error",
            "message": "Please select only 5 pdf files"
        }
    else:
        return {
            "status": "success",
            "message": "PDF files are valid"
        }