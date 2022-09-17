import json, requests

def get_thought():
    data=[]
    try:
        # url = 'https://zenquotes.io/api/today'
        url = f'http://localhost:5000/api/thought'
        # getting the content of the request
        response = requests.get(url)
        # throwing exception in case of api error
        response.raise_for_status()
        # store all the data to send in a dictionary
        data = response.text
    except:
        data = {
            'error': 'An error has occurred.'
        }
    # returning the data in json format
    return data