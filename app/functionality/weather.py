import json, requests

# function to convert kelvin to celsius
def convert_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

def get_weather():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=mangalore&appid=f5990901916de44b03db0a2d1c42140d'
    # getting the content of the request
    response = requests.get(url)
    # throwing exception in case of api error
    response.raise_for_status()
    # converting the response from json to python dictionary
    weather_data = json.loads(response.text)
    # store all the data to send in a dictionary
    data_to_get = {
        'temp': convert_to_celsius(weather_data['main']['temp']),
        'feels_like': convert_to_celsius(weather_data['main']['feels_like']),
        'humidity': weather_data['main']['humidity'],
        'description': weather_data['weather'][0]['description'],
        'wind_speed': weather_data['wind']['speed']
    }
    # returning the data in json format
    return data_to_get