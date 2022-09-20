import json, requests, os

# Function to convert kelvin to celsius
def convert_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

def get_weather(location):
    data = {}
    try:
        url = os.getenv('BACKEND_URL_DEVELOPMENT')+f'/api/weather/{location}'

        # Getting the content of the request
        response = requests.get(url)

        # Throwing exception in case of api error
        response.raise_for_status()
        
        # Store all the data to send in a dictionary
        weather_data = json.loads(response.text)['payload']
        data = {
            'temp': convert_to_celsius(weather_data['main']['temp']),
            'feels_like': convert_to_celsius(weather_data['main']['feels_like']),
            'icon': weather_data['weather'][0]['icon'],
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
    # Returning the data in json format
    return data