import requests, re

# Function to validate the inputs from the signup page
def validate_register(name, email, password):
    # Stripping the name and storing it in new_name variable
    new_name = name.strip()
    # Regular expression for checking if the email is valid or not
    emailRe = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    # Re for checking if the phone no. is valid or not
    passwordRe = re.compile(r'.{2,20}')
    # Checking if the name is not a decimal
    if new_name.isdecimal():
        return {
            "status": "error",
            "message": "Please enter your name in the correct format"
        }
    # Checking if the email is valid
    if len(emailRe.findall(email)) < 1:
        return {
            "status": "error",
            "message": "Please enter your email in the correct format"
        }
    # Checking if the password is valid
    if len(passwordRe.findall(password)) < 1:
        return {
            "status": "error",
            "message": "Please enter your password"
        }
    else:
        return {
            "status": "success",
            "message": "Registration successful"
        }


def validate_email(email):
    emailRe = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    # Passing the email to the api to validate
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email}
    )
    # Getting the data from the response
    status = response.json()['status']
    # Checking if the status is valid
    if status == "valid" and len(emailRe.findall(email)) >= 1:
        return {
            "status": "success",
            "message": "Email is valid"
        }
    # Checking if the status is invalid
    elif status == "invalid":
        return {
            "status": "error",
            "message": "Please enter a valid email address!"
        }
    else:
        return {
            "status": "error",
            "message": "Please enter a valid email address!"
        }

# Input validation for login
def validate_login(name, password):
    passwordRe = re.compile(r'.{2,20}')
    # Stripping the name and storing it in new_name variable
    new_name = name.strip()
    if new_name.isdecimal():
        return {
            "status": "error",
            "message": "Please enter your name in the correct format"
        }
    # Checking if the password is valid
    if len(passwordRe.findall(password)) < 1:
        return {
            "status": "error",
            "message": "Please enter your password"
        }
    else:
        return {
            "status": "success",
            "message": "Login successful"
        }


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