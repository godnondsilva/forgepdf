import json, requests, os

def get_thought():
    data=[]
    try:
        url = os.getenv('BACKEND_URL')+'/api/thought'
        # Getting the content of the request
        response = requests.get(url)
        # Throwing exception in case of api error
        response.raise_for_status()
        # Store all the data to send in a dictionary
        data = json.loads(response.text)['payload']
    except:
        data = {
            'error': 'An error has occurred.'
        }
    # Returning the data in json format
    return data