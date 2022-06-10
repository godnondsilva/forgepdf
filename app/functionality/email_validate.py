import json, requests
from app.store import state

def validate():
    # getting the email from the state
    email = state.get_email()
    # passing the email to the api to validate
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email}
    )
    # getting the data from the response
    status = response.json()['status']
    # checking if the status is valid
    if status == "valid":
        return {"response": True}
    # checking if the status is invalid
    elif status == "invalid":
        return {"error": "Please enter a valid email address!"}
    # all other cases
    else:
        return {"error": "Please enter a valid email address!"}