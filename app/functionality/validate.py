import requests, re

# function to validate the inputs from the signup page
def validate_register(name, email, password):
    # stripping the name and storing it in new_name variable
    new_name = name.strip()
    # re for checking if the email is valid or not
    emailRe = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    # re for checking if the phone no. is valid or not
    passwordRe = re.compile(r'.{2,20}')
    # checking if the name is not a decimal
    if new_name.isdecimal():
        return {"error": "Please enter your name in the correct format"}
    # checking if the email is valid
    if len(emailRe.findall(email)) < 1:
        return {"error": "Please enter your email in the correct format"}
    # checking if the password is valid
    if len(passwordRe.findall(password)) < 1:
        return {"error": "Please enter your password"}
    else:
        return True


def validate_email(email):
    emailRe = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    # passing the email to the api to validate
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email}
    )
    # getting the data from the response
    status = response.json()['status']
    # checking if the status is valid
    if status == "valid" and len(emailRe.findall(email)) >= 1:
        return {"response": True}
    # checking if the status is invalid
    elif status == "invalid":
        return {"error": "Please enter a valid email address!"}
    # all other cases
    else:
        return {"error": "Please enter a valid email address!"}

#input validation for login
def validate_login(name, password):
    passwordRe = re.compile(r'.{2,20}')
    # stripping the name and storing it in new_name variable
    new_name = name.strip()
    if new_name.isdecimal():
        return {"error": "Please enter your name in the correct format"}
    if len(passwordRe.findall(password)) < 1:
        return {"error": "Please enter your password"}
    else:
        return True


# function to check whether the string given is containing only numbers
def validate_split(start, end):
    # the variables start and end are string variables
    # convert to int for comparing values
    #if starting range is greater than endingrange
    if (int(start) > int(end)):
        return {"error": "Starting range cannt be greater than ending range!!"}
    if start.isdecimal()==False and end.isdecimal()==False:
        return {"error": "Please enter a valid range"}
    else:
        return True


# function for validating the inputs from encrypt pdf page
# validates the password field
def validate_encrypt(password):
    # if the password is empty
    if len(password) == 0:
        return {"error": "Please enter a valid password"}
    else:
        return True

# function for validating the inputs from decrypt pdf page
# validates the password field
def validate_decrypt(password):
    # if the password is empty
    if len(password) == 0:
        return {"error": "Please enter a valid password"}
    else:
        return True

# function for validating the inputs from extract pdf page
# validates the pdf_path which is the absolute path of the pdf file
def validate_extract(pdf_path):
    # if the path is empty
    if len(pdf_path) == 0:
        return {"error": "Please input a valid pdf path"}
    else:
        return True
