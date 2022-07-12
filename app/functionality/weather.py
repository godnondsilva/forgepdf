import json, requests, os

# function to convert kelvin to celsius
def convert_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

def get_weather(location):
    data = {}
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={os.getenv("WEATHER_API_KEY")}'
        # getting the content of the request
        response = requests.get(url)
        # throwing exception in case of api error
        response.raise_for_status()
        # converting the response from json to python dictionary
        weather_data = json.loads(response.text)
        # store all the data to send in a dictionary
        data = {
            'temp': convert_to_celsius(weather_data['main']['temp']),
            'feels_like': convert_to_celsius(weather_data['main']['feels_like']),
            'main': weather_data['weather'][0]['main'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],
            'pressure': weather_data['main']['pressure'],
        }
    except:
        data = {
            'error': 'An error has occurred.'
        }
    # returning the data in json format
    return data