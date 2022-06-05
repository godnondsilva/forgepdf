import requests, json

# this function is used to call the API and return the response
def getEmailValidate(email):
    # trying to get the response from the api and storing it in the emailData variable
    try:
        response = requests.get('http://localhost:5000/emailvalidate?email='+email)
        emailData = json.loads(response.text)
    # if there was an error while retrieving the data, we return an the following dictionary
    # this is most likely called if the server is not running
    except:
        emailData = json.dumps({"error": "Could not connect to the server, please run the server first"})
        emailData = json.loads(emailData)
    # returning the emailData variable
    return emailData
    
    