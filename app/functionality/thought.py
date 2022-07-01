import json, requests

def get_thought():
    url = 'https://zenquotes.io/api/today'
    # getting the content of the request
    response = requests.get(url)
    # throwing exception in case of api error
    response.raise_for_status()
    # converting the response from json to python dictionary
    thought_data = json.loads(response.text)
    # store all the data to send in a dictionary
    # returning the data in json format
    return thought_data[0]['q']