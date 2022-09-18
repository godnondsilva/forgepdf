import json, requests, os

def get_thought():
    data=[]
    try:
        url = os.getenv('BACKEND_URL_DEVELOPMENT')+'/api/thought'
        # getting the content of the request
        response = requests.get(url)
        # throwing exception in case of api error
        response.raise_for_status()
        # store all the data to send in a dictionary
        data = json.loads(response.text)['payload']
    except:
        data = {
            'error': 'An error has occurred.'
        }
    # returning the data in json format
    return data